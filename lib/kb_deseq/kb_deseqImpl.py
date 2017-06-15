# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from kb_deseq.Utils.DESeqUtil import DESeqUtil
#END_HEADER


class kb_deseq:
    '''
    Module Name:
    kb_deseq

    Module Description:
    A KBase module: kb_deseq
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_deseq.git"
    GIT_COMMIT_HASH = "be1922b71d5b40a706400d115c066114e04f3b3a"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_deseq2_app(self, ctx, params):
        """
        run_deseq2_app: run DESeq2 app
        ref: https://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html
        :param params: instance of type "DESeqInput" (required params:
           expressionset_ref: ExpressionSet object reference
           diff_expression_obj_name: RNASeqDifferetialExpression object name
           filtered_expression_matrix_name: name of output object filtered
           expression matrix expr_condition_list: conditions for expression
           set object alpha_cutoff: q value cutoff num_threads: number of
           threads workspace_name: the name of the workspace it gets saved to
           optional params: fold_scale_type: one of ["linear", "log2+1",
           "log10+1"] fold_change_cutoff: fold change cutoff) -> structure:
           parameter "expressionset_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "diff_expression_obj_name" of String,
           parameter "filtered_expression_matrix_name" of String, parameter
           "expr_condition_list" of list of type "ExpressionConditionList" ->
           structure: parameter "condition_name" of String, parameter
           "expression_refs" of list of String, parameter "alpha_cutoff" of
           Double, parameter "num_threads" of Long, parameter
           "workspace_name" of String, parameter "fold_scale_type" of String,
           parameter "fold_change_cutoff" of Double
        :returns: instance of type "DESeqResult" (result_directory: folder
           path that holds all files generated by run_deseq2_app
           diff_expression_obj_ref: generated RNASeqDifferetialExpression
           object reference filtered_expression_matrix_ref: generated
           ExpressionMatrix object reference report_name: report name
           generated by KBaseReport report_ref: report reference generated by
           KBaseReport) -> structure: parameter "result_directory" of String,
           parameter "diff_expression_obj_ref" of type "obj_ref" (An X/Y/Z
           style reference), parameter "filtered_expression_matrix_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter "report_name"
           of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_deseq2_app
        print '--->\nRunning kb_deseq.run_deseq2_app\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        deseq_runner = DESeqUtil(self.config)
        returnVal = deseq_runner.run_deseq2_app(params)
        #END run_deseq2_app

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_deseq2_app return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
