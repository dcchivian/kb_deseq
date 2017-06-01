import time
import json
import os
import uuid
import errno
import subprocess
import math

# from DataFileUtil.DataFileUtilClient import DataFileUtil
# from Workspace.WorkspaceClient import Workspace as Workspace
from KBaseReport.KBaseReportClient import KBaseReport
# from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
# from ReadsAlignmentUtils.ReadsAlignmentUtilsClient import ReadsAlignmentUtils


def log(message, prefix_newline=False):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(('\n' if prefix_newline else '') + '{0:.2f}'.format(time.time()) + ': ' + str(message))


class DESeqUtil:

    def _validate_run_deseq2_app_params(self, params):
        """
        _validate_run_stringtie_params:
                validates params passed to run_stringtie method
        """

        log('Start validating run_stringtie params')

        # check for required parameters
        for p in ['expressionset_ref', 'diff_expression_obj_name', 'filtered_expr_matrix',
                  'workspace_name']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

    def _mkdir_p(self, path):
        """
        _mkdir_p: make directory for given path
        """
        if not path:
            return
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def _generate_report(self, obj_ref, workspace_name):
        """
        _generate_report: generate summary report
        """
        log('creating report')
        uuid_string = str(uuid.uuid4())
        upload_message = 'Run DESeq App Finished\n\n'

        info = self.ws.get_object_info3({"objects": [{"ref": obj_ref}]})['infos'][0]

        upload_message += "Saved Differetial Expression Object: {}\n".format(info[1])

        report_params = {
              'message': upload_message,
              'workspace_name': workspace_name,
              'report_object_name': 'kb_upload_mothods_report_' + uuid_string}

        kbase_report_client = KBaseReport(self.callback_url, token=self.token)
        output = kbase_report_client.create_extended_report(report_params)

        report_output = {'report_name': output['name'], 'report_ref': output['ref']}

        return report_output

    def _get_count_matrix_file(self, expressionset_ref):
        pass

    def _save_diff_expression(self, result_directory, expressionset_ref,
                              workspace_name, diff_expression_obj_name):
        pass

    def __init__(self, config):
        self.ws_url = config["workspace-url"]
        self.callback_url = config['SDK_CALLBACK_URL']
        self.token = config['KB_AUTH_TOKEN']
        self.shock_url = config['shock-url']
        # self.dfu = DataFileUtil(self.callback_url)
        # self.gfu = GenomeFileUtil(self.callback_url)
        # self.rau = ReadsAlignmentUtils(self.callback_url)
        # self.ws = Workspace(self.ws_url, token=self.token)
        self.scratch = config['scratch']
        # self.scratch = os.path.join(config['scratch'], str(uuid.uuid4()))
        # self._mkdir_p(self.scratch)

    def run_deseq2_app(self, params):
        """
        run_deseq2_app: run DESeq2 app
        (https://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)

        required params:
        expressionset_ref: ExpressionSet object reference
        diff_expression_obj_name: RNASeqDifferetialExpression object name
        filtered_expr_matrix: name of output object filtered expression matrix
        workspace_name: the name of the workspace it gets saved to

        optional params:
        fold_scale_type: one of ["linear", "log2+1", "log10+1"]
        alpha_cutoff: q value cutoff

        return:
        result_directory: folder path that holds all files generated by run_deseq2_app
        diff_expression_obj_ref: generated RNASeqDifferetialExpression object reference
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
        """
        log('--->\nrunning DESeqUtil.run_deseq2_app\n' +
            'params:\n{}'.format(json.dumps(params, indent=1)))

        self._validate_run_deseq2_app_params(params)

        result_directory = os.path.join(self.scratch, str(uuid.uuid4()))
        self._mkdir_p(result_directory)

        # input files
        expressionset_ref = params.get('expressionset_ref')
        params['count_matrix_file'] = self._get_count_matrix_file(expressionset_ref)

        diff_expression_obj_ref = self._save_diff_expression(result_directory,
                                                             expressionset_ref,
                                                             params.get('workspace_name'),
                                                             params.get('diff_expression_obj_name'))

        returnVal = {'result_directory': result_directory,
                     'diff_expression_obj_ref': diff_expression_obj_ref}

        report_output = self._generate_report(diff_expression_obj_ref, params.get('workspace_name'))
        returnVal.update(report_output)

        return returnVal