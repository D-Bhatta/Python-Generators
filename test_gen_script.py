import gen_script 
g = gen_script.Generators()
class TestObject(object):
    def test_using_generators(self):
        a = g.using_generators()
        b = [(1461, 1461, 1461),
        'Infinite sequence nums = 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149  150  151  152  153  154  155  156  157  158  159  160  161  162  163  164  165  166  167  168  169  170  171  172  173  174  175  176  177  178  179  180  181  182  183  184  185  186  187  188  189  190  191  192  193  194  195  196  197  198  199  200  201  202  203  204  205  206  207  208  209  210  211  212  213  214  215  216  217  218  219  220  221  222  223  224  225  226  227  228  229  230  231  232  233  234  235  236  237  238  239  240  241  242  243  244  245  246  247  248  249  250  251  252  253  254  255  256  257  258  259  260  261  262  263  264  265  266  267  268  269  270  271  272  273  274  275  276  277  278  279  280  281  282  283  284  285  286  287  288  289  290  291  292  293  294  295  296  297  298  299  300  301  302  303  304  305  306  307  308  309  310  311  312  313  314  315  316  317  318  319  320  321  322  323  324  325  326  327  328  329  330  331  332  333  334  335  336  337  338  339  340  341  342  343  344  345  346  347  348  349  350  351  352  353  354  355  356  357  358  359  360  361  362  363  364  365  366  367  368  369  370  371  372  373  374  375  376  377  378  379  380  381  382  383  384  385  386  387  388  389  390  391  392  393  394  395  396  397  398  399  400  401  402  403  404  405  406  407  408  409  410  411  412  413  414  415  416  417  418  419  420  421  422  423  424  425  426  427  428  429  430  431  432  433  434  435  436  437  438  439  440  441  442  443  444  445  446  447  448  449  450  451  452  453  454  455  456  457  458  459  460  461  462  463  464  465  466  467  468  469  470  471  472  473  474  475  476  477  478  479  480  481  482  483  484  485  486  487  488  489  490  491  492  493  494  495  496  497  498  499  500  501  502  503  504  505  506  507  508  509  510  511  512  513  514  515  516  517  518  519  520  521  522  523  524  525  526  527  528  529  530  531  532  533  534  535  536  537  538  539  540  541  542  543  544  545  546  547  548  549  550  551  552  553  554  555  556  557  558  559  560  561  562  563  564  565  566  567  568  569  570  571  572  573  574  575  576  577  578  579  580  581  582  583  584  585  586  587  588  589  590  591  592  593  594  595  596  597  598  599  600  601  602  603  604  605  606  607  608  609  610  611  612  613  614  615  616  617  618  619  620  621  622  623  624  625  626  627  628  629  630  631  632  633  634  635  636  637  638  639  640  641  642  643  644  645  646  647  648  649  650  651  652  653  654  655  656  657  658  659  660  661  662  663  664  665  666  667  668  669  670  671  672  673  674  675  676  677  678  679  680  681  682  683  684  685  686  687  688  689  690  691  692  693  694  695  696  697  698  699  700  701  702  703  704  705  706  707  708  709  710  711  712  713  714  715  716  717  718  719  720  721  722  723  724  725  726  727  728  729  730  731  732  733  734  735  736  737  738  739  740  741  742  743  744  745  746  747  748  749  750  751  752  753  754  755  756  757  758  759  760  761  762  763  764  765  766  767  768  769  770  771  772  773  774  775  776  777  778  779  780  781  782  783  784  785  786  787  788  789  790  791  792  793  794  795  796  797  798  799  800  801  802  803  804  805  806  807  808  809  810  811  812  813  814  815  816  817  818  819  820  821  822  823  824  825  826  827  828  829  830  831  832  833  834  835  836  837  838  839  840  841  842  843  844  845  846  847  848  849  850  851  852  853  854  855  856  857  858  859  860  861  862  863  864  865  866  867  868  869  870  871  872  873  874  875  876  877  878  879  880  881  882  883  884  885  886  887  888  889  890  891  892  893  894  895  896  897  898  899  900  901  902  903  904  905  906  907  908  909  910  911  912  913  914  915  916  917  918  919  920  921  922  923  924  925  926  927  928  929  930  931  932  933  934  935  936  937  938  939  940  941  942  943  944  945  946  947  948  949  950  951  952  953  954  955  956  957  958  959  960  961  962  963  964  965  966  967  968  969  970  971  972  973  974  975  976  977  978  979  980  981  982  983  984  985  986  987  988  989  990  991  992  993  994  995  996  997  998  999  ',
        'Second infinite sequence = 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149  150  151  152  153  154  155  156  157  158  159  160  161  162  163  164  165  166  167  168  169  170  171  172  173  174  175  176  177  178  179  180  181  182  183  184  185  186  187  188  189  190  191  192  193  194  195  196  197  198  199  200  201  202  203  204  205  206  207  208  209  210  211  212  213  214  215  216  217  218  219  220  221  222  223  224  225  226  227  228  229  230  231  232  233  234  235  236  237  238  239  240  241  242  243  244  245  246  247  248  249  250  251  252  253  254  255  256  257  258  259  260  261  262  263  264  265  266  267  268  269  270  271  272  273  274  275  276  277  278  279  280  281  282  283  284  285  286  287  288  289  290  291  292  293  294  295  296  297  298  299  300  301  302  303  304  305  306  307  308  309  310  311  312  313  314  315  316  317  318  319  320  321  322  323  324  325  326  327  328  329  330  331  332  333  334  335  336  337  338  339  340  341  342  343  344  345  346  347  348  349  350  351  352  353  354  355  356  357  358  359  360  361  362  363  364  365  366  367  368  369  370  371  372  373  374  375  376  377  378  379  380  381  382  383  384  385  386  387  388  389  390  391  392  393  394  395  396  397  398  399  400  401  402  403  404  405  406  407  408  409  410  411  412  413  414  415  416  417  418  419  420  421  422  423  424  425  426  427  428  429  430  431  432  433  434  435  436  437  438  439  440  441  442  443  444  445  446  447  448  449  450  451  452  453  454  455  456  457  458  459  460  461  462  463  464  465  466  467  468  469  470  471  472  473  474  475  476  477  478  479  480  481  482  483  484  485  486  487  488  489  490  491  492  493  494  495  496  497  498  499  500  501  502  503  504  505  506  507  508  509  510  511  512  513  514  515  516  517  518  519  520  521  522  523  524  525  526  527  528  529  530  531  532  533  534  535  536  537  538  539  540  541  542  543  544  545  546  547  548  549  550  551  552  553  554  555  556  557  558  559  560  561  562  563  564  565  566  567  568  569  570  571  572  573  574  575  576  577  578  579  580  581  582  583  584  585  586  587  588  589  590  591  592  593  594  595  596  597  598  599  600  601  602  603  604  605  606  607  608  609  610  611  612  613  614  615  616  617  618  619  620  621  622  623  624  625  626  627  628  629  630  631  632  633  634  635  636  637  638  639  640  641  642  643  644  645  646  647  648  649  650  651  652  653  654  655  656  657  658  659  660  661  662  663  664  665  666  667  668  669  670  671  672  673  674  675  676  677  678  679  680  681  682  683  684  685  686  687  688  689  690  691  692  693  694  695  696  697  698  699  700  701  702  703  704  705  706  707  708  709  710  711  712  713  714  715  716  717  718  719  720  721  722  723  724  725  726  727  728  729  730  731  732  733  734  735  736  737  738  739  740  741  742  743  744  745  746  747  748  749  750  751  752  753  754  755  756  757  758  759  760  761  762  763  764  765  766  767  768  769  770  771  772  773  774  775  776  777  778  779  780  781  782  783  784  785  786  787  788  789  790  791  792  793  794  795  796  797  798  799  800  801  802  803  804  805  806  807  808  809  810  811  812  813  814  815  816  817  818  819  820  821  822  823  824  825  826  827  828  829  830  831  832  833  834  835  836  837  838  839  840  841  842  843  844  845  846  847  848  849  850  851  852  853  854  855  856  857  858  859  860  861  862  863  864  865  866  867  868  869  870  871  872  873  874  875  876  877  878  879  880  881  882  883  884  885  886  887  888  889  890  891  892  893  894  895  896  897  898  899  900  901  902  903  904  905  906  907  908  909  910  911  912  913  914  915  916  917  918  919  920  921  922  923  924  925  926  927  928  929  930  931  932  933  934  935  936  937  938  939  940  941  942  943  944  945  946  947  948  949  950  951  952  953  954  955  956  957  958  959  960  961  962  963  964  965  966  967  968  969  970  971  972  973  974  975  976  977  978  979  980  981  982  983  984  985  986  987  988  989  990  991  992  993  994  995  996  997  998  999  ',
        'Palindrome number sequence: 11  22  33  44  55  66  77  88  99  101  111  121  131  141  151  161  171  181  191  202  212  222  232  242  252  262  272  282  292  303  313  323  333  343  353  363  373  383  393  404  414  424  434  444  454  464  474  484  494  505  515  525  535  545  555  565  575  585  595  606  616  626  636  646  656  666  676  686  696  707  717  727  737  747  757  767  777  787  797  808  818  828  838  848  858  868  878  888  898  909  919  929  939  949  959  969  979  989  999  1001  1111  1221  1331  1441  1551  1661  1771  1881  1991  2002  2112  2222  2332  2442  2552  2662  2772  2882  2992  3003  3113  3223  3333  3443  3553  3663  3773  3883  3993  4004  4114  4224  4334  4444  4554  4664  4774  4884  4994  5005  5115  5225  5335  5445  5555  5665  5775  5885  5995  6006  6116  6226  6336  6446  6556  6666  6776  6886  6996  7007  7117  7227  7337  7447  7557  7667  7777  7887  7997  8008  8118  8228  8338  8448  8558  8668  8778  8888  8998  9009  9119  9229  9339  9449  9559  9669  9779  9889  9999  10001  10101  10201  10301  10401  10501  10601  10701  10801  10901  11011  11111  11211  11311  11411  11511  11611  11711  11811  11911  12021  12121  12221  12321  12421  12521  12621  12721  12821  12921  13031  13131  13231  13331  13431  13531  13631  13731  13831  13931  14041  14141  14241  14341  14441  14541  14641  14741  14841  14941  15051  15151  15251  15351  15451  15551  15651  15751  15851  15951  16061  16161  16261  16361  16461  16561  16661  16761  16861  16961  17071  17171  17271  17371  17471  17571  17671  17771  17871  17971  18081  18181  18281  18381  18481  18581  18681  18781  18881  18981  19091  19191  19291  19391  19491  19591  19691  19791  19891  19991  20002  20102  20202  20302  20402  20502  20602  20702  20802  20902  21012  21112  21212  21312  21412  21512  21612  21712  21812  21912  22022  22122  22222  22322  22422  22522  22622  22722  22822  22922  23032  23132  23232  23332  23432  23532  23632  23732  23832  23932  24042  24142  24242  24342  24442  24542  24642  24742  24842  24942  25052  25152  25252  25352  25452  25552  25652  25752  25852  25952  26062  26162  26262  26362  26462  26562  26662  26762  26862  26962  27072  27172  27272  27372  27472  27572  27672  27772  27872  27972  28082  28182  28282  28382  28482  28582  28682  28782  28882  28982  29092  29192  29292  29392  29492  29592  29692  29792  29892  29992  30003  30103  30203  30303  30403  30503  30603  30703  30803  30903  31013  31113  31213  31313  31413  31513  31613  31713  31813  31913  32023  32123  32223  32323  32423  32523  32623  32723  32823  32923  33033  33133  33233  33333  33433  33533  33633  33733  33833  33933  34043  34143  34243  34343  34443  34543  34643  34743  34843  34943  35053  35153  35253  35353  35453  35553  35653  35753  35853  35953  36063  36163  36263  36363  36463  36563  36663  36763  36863  36963  37073  37173  37273  37373  37473  37573  37673  37773  37873  37973  38083  38183  38283  38383  38483  38583  38683  38783  38883  38983  39093  39193  39293  39393  39493  39593  39693  39793  39893  39993  40004  40104  40204  40304  40404  40504  40604  40704  40804  40904  41014  41114  41214  41314  41414  41514  41614  41714  41814  41914  42024  42124  42224  42324  42424  42524  42624  42724  42824  42924  43034  43134  43234  43334  43434  43534  43634  43734  43834  43934  44044  44144  44244  44344  44444  44544  44644  44744  44844  44944  45054  45154  45254  45354  45454  45554  45654  45754  45854  45954  46064  46164  46264  46364  46464  46564  46664  46764  46864  46964  47074  47174  47274  47374  47474  47574  47674  47774  47874  47974  48084  48184  48284  48384  48484  48584  48684  48784  48884  48984  49094  49194  49294  49394  49494  49594  49694  49794  49894  49994  50005  50105  50205  50305  50405  50505  50605  50705  50805  50905  51015  51115  51215  51315  51415  51515  51615  51715  51815  51915  52025  52125  52225  52325  52425  52525  52625  52725  52825  52925  53035  53135  53235  53335  53435  53535  53635  53735  53835  53935  54045  54145  54245  54345  54445  54545  54645  54745  54845  54945  55055  55155  55255  55355  55455  55555  55655  55755  55855  55955  56065  56165  56265  56365  56465  56565  56665  56765  56865  56965  57075  57175  57275  57375  57475  57575  57675  57775  57875  57975  58085  58185  58285  58385  58485  58585  58685  58785  58885  58985  59095  59195  59295  59395  59495  59595  59695  59795  59895  59995  60006  60106  60206  60306  60406  60506  60606  60706  60806  60906  61016  61116  61216  61316  61416  61516  61616  61716  61816  61916  62026  62126  62226  62326  62426  62526  62626  62726  62826  62926  63036  63136  63236  63336  63436  63536  63636  63736  63836  63936  64046  64146  64246  64346  64446  64546  64646  64746  64846  64946  65056  65156  65256  65356  65456  65556  65656  65756  65856  65956  66066  66166  66266  66366  66466  66566  66666  66766  66866  66966  67076  67176  67276  67376  67476  67576  67676  67776  67876  67976  68086  68186  68286  68386  68486  68586  68686  68786  68886  68986  69096  69196  69296  69396  69496  69596  69696  69796  69896  69996  70007  70107  70207  70307  70407  70507  70607  70707  70807  70907  71017  71117  71217  71317  71417  71517  71617  71717  71817  71917  72027  72127  72227  72327  72427  72527  72627  72727  72827  72927  73037  73137  73237  73337  73437  73537  73637  73737  73837  73937  74047  74147  74247  74347  74447  74547  74647  74747  74847  74947  75057  75157  75257  75357  75457  75557  75657  75757  75857  75957  76067  76167  76267  76367  76467  76567  76667  76767  76867  76967  77077  77177  77277  77377  77477  77577  77677  77777  77877  77977  78087  78187  78287  78387  78487  78587  78687  78787  78887  78987  79097  79197  79297  79397  79497  79597  79697  79797  79897  79997  80008  80108  80208  80308  80408  80508  80608  80708  80808  80908  81018  81118  81218  81318  81418  81518  81618  81718  81818  81918  82028  82128  82228  82328  82428  82528  82628  82728  82828  82928  83038  83138  83238  83338  83438  83538  83638  83738  83838  83938  84048  84148  84248  84348  84448  84548  84648  84748  84848  84948  85058  85158  85258  85358  85458  85558  85658  85758  85858  85958  86068  86168  86268  86368  86468  86568  86668  86768  86868  86968  87078  87178  87278  87378  87478  87578  87678  87778  87878  87978  88088  88188  88288  88388  88488  88588  88688  88788  88888  88988  89098  89198  89298  89398  89498  89598  89698  89798  89898  89998  90009  90109  90209  90309  90409  90509  90609  90709  90809  90909  91019  91119  91219  91319  91419  91519  91619  91719  91819  91919  92029  92129  92229  92329  92429  92529  92629  92729  92829  92929  93039  93139  93239  93339  93439  93539  93639  93739  93839  93939  94049  94149  94249  94349  94449  94549  94649  94749  94849  94949  95059  95159  95259  95359  95459  95559  95659  95759  95859  95959  96069  96169  96269  96369  96469  96569  96669  96769  96869  96969  97079  97179  97279  97379  97479  97579  97679  97779  97879  97979  98089  98189  98289  98389  98489  98589  98689  98789  98889  98989  99099  99199  99299  99399  99499  99599  99699  99799  99899  99999  100001  101101  102201  ']
        assert a == b , "Output list doesn't match in using_generators()"