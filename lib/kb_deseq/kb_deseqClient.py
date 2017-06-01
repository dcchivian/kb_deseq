# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_deseq(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_deseq2_app(self, params, context=None):
        """
        run_deseq2_app: run DESeq2 app
        ref: https://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html
        :param params: instance of type "DESeqInput" (required params:
           expressionset_ref: ExpressionSet object reference
           diff_expression_obj_name: RNASeqDifferetialExpression object name
           filtered_expr_matrix: name of output object filtered expression
           matrix workspace_name: the name of the workspace it gets saved to
           optional params: fold_scale_type: one of ["linear", "log2+1",
           "log10+1"] alpha_cutoff: q value cutoff fold_change_cutoff: fold
           change cutoff maximum_num_genes: maximum gene numbers) ->
           structure: parameter "expressionset_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "diff_expression_obj_name" of
           String, parameter "filtered_expr_matrix" of String, parameter
           "workspace_name" of String, parameter "num_threads" of Long,
           parameter "expr_ids_list" of type "ExperimentGroupIDsList" ->
           structure: parameter "group_name1" of String, parameter
           "expr_ids1" of list of String, parameter "group_name2" of String,
           parameter "expr_ids2" of list of String, parameter
           "fold_scale_type" of String, parameter "alpha_cutoff" of Double,
           parameter "fold_change_cutoff" of Double, parameter
           "maximum_num_genes" of Long
        :returns: instance of type "DESeqResult" (result_directory: folder
           path that holds all files generated by run_deseq2_app
           diff_expression_obj_ref: generated RNASeqDifferetialExpression
           object reference report_name: report name generated by KBaseReport
           report_ref: report reference generated by KBaseReport) ->
           structure: parameter "result_directory" of String, parameter
           "diff_expression_obj_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method(
            'kb_deseq.run_deseq2_app',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_deseq.status',
                                        [], self._service_ver, context)
