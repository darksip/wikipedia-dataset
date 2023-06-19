---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
pretty_name: Wikipedia
paperswithcode_id: null
license:
- cc-by-sa-3.0
- gfdl
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
source_datasets:
- original
multilinguality:
- multilingual
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
language:
# - aa  - closed and no dump
- ab
- ace
- ady
- af
- ak
- als
- alt
- am
- ami
- an
- ang
- anp
- ar
- arc
- ary
- arz
- as
- ast
- atj
- av
- avk
- awa
- ay
- az
- azb
- ba
- ban
- bar
# - bat-smg - see bcp47 below
- bcl
# - be-x-old - see bcp47 below
- be
- bg
- bh
- bi
- bjn
- blk
- bm
- bn
- bo
- bpy
- br
- bs
- bug
- bxr
- ca
# - cbk-zam - see bcp47 below
- cdo
- ce
- ceb
- ch
- cho  # closed
- chr
- chy
- ckb
- co
- cr
- crh
- cs
- csb
- cu
- cv
- cy
- da
- dag
- de
- din
- diq
- dsb
- dty
- dv
- dz
- ee
- el
- eml
- eo
- es
- et
- eu
- ext
- fa
- fat
- ff
- fi
# - fiu-vro - see bcp47 below
- fj
- fo
- fr
- frp
- frr
- fur
- fy
- ga
- gag
- gan
- gcr
- gd
- gl
- glk
- gn
- gom
- gor
- got
- gu
- guc
- gur
- guw
- gv
- ha
- hak
- haw
- he
- hi
- hif
- ho  # closed
- hr
- hsb
- ht
- hu
- hy
- hyw
# - hz  - closed and no dump
- ia
- id
- ie
- ig
- ii  # closed
- ik
- ilo
- inh
- io
- is
- it
- iu
- ja
- jam
- jbo
- jv
- ka
- kaa
- kab
- kbd
- kbp
- kcg
- kg
- ki
- kj  # closed
- kk
- kl
- km
- kn
- ko
- koi
# - kr - closed and no dump
- krc
- ks
- ksh
- ku
- kv
- kw
- ky
- la
- lad
- lb
- lbe
- lez
- lfn
- lg
- li
- lij
- lld
- lmo
- ln
- lo
- lrc  # closed
- lt
- ltg
- lv
- mad
- mai
# - map-bms - see bcp47 below
- mdf
- mg
- mh
- mhr
- mi
- min
- mk
- ml
- mn
- mni
- mnw
- mr
- mrj
- ms
- mt
- mus  # closed
- mwl
- my
- myv
- mzn
# - na - closed and no dump
- nah
- nap
# - nds-nl - see bcp47 below
- nds
- ne
- new
- ng  # closed
- nia
- nl
- nn
- no
- nov
- nqo
- nrm
- nso
- nv
- ny
- oc
- olo
- om
- or
- os
- pa
- pag
- pam
- pap
- pcd
- pcm
- pdc
- pfl
- pi
- pih
- pl
- pms
- pnb
- pnt
- ps
- pt
- pwn
- qu
- rm
- rmy
- rn
- ro
# - roa-rup - see bcp47 below
# - roa-tara - see bcp47 below
- ru
- rue
- rw
- sa
- sah
- sat
- sc
- scn
- sco
- sd
- se
- sg
- sh
- shi
- shn
- si
# - simple - see bcp47 below
- sk
- skr
- sl
- sm
- smn
- sn
- so
- sq
- sr
- srn
- ss
- st
- stq
- su
- sv
- sw
- szl
- szy
- ta
- tay
- tcy
- te
- tet
- tg
- th
- ti
- tk
- tl
- tn
- to
- tpi
- tr
- trv
- ts
- tt
- tum
- tw
- ty
- tyv
- udm
- ug
- uk
- ur
- uz
- ve
- vec
- vep
- vi
- vls
- vo
- wa
- war
- wo
- wuu
- xal
- xh
- xmf
- yi
- yo
- za
- zea
- zh
# - zh-classical - see bcp47 below
# - zh-min-nan - see bcp47 below
# - zh-yue - see bcp47 below
- zu
language_bcp47:
- bat-smg
- be-x-old
- cbk-zam
- fiu-vro
- map-bms
- nds-nl
- roa-rup
- roa-tara
- simple
- zh-classical
- zh-min-nan
- zh-yue
dataset_info:
- config_name: 20230601.ab
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4183525
    num_examples: 6114
  download_size: 1172328
  dataset_size: 4183525
- config_name: 20230601.ace
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4887561
    num_examples: 12839
  download_size: 1473823
  dataset_size: 4887561
- config_name: 20230601.ady
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 613082
    num_examples: 609
  download_size: 280249
  dataset_size: 613082
- config_name: 20230601.af
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 220678901
    num_examples: 108170
  download_size: 121238071
  dataset_size: 220678901
- config_name: 20230601.ak
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 189
    num_examples: 1
  download_size: 3045
  dataset_size: 189
- config_name: 20230601.als
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 80615079
    num_examples: 29804
  download_size: 48883379
  dataset_size: 80615079
- config_name: 20230601.alt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5786027
    num_examples: 1082
  download_size: 2401701
  dataset_size: 5786027
- config_name: 20230601.am
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24009050
    num_examples: 13839
  download_size: 10615909
  dataset_size: 24009050
- config_name: 20230601.ami
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3865236
    num_examples: 1570
  download_size: 2006639
  dataset_size: 3865236
- config_name: 20230601.an
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 56295233
    num_examples: 43744
  download_size: 29055888
  dataset_size: 56295233
- config_name: 20230601.ang
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2854073
    num_examples: 4019
  download_size: 1756372
  dataset_size: 2854073
- config_name: 20230601.anp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9055032
    num_examples: 2736
  download_size: 3270423
  dataset_size: 9055032
- config_name: 20230601.ar
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3052201469
    num_examples: 1205403
  download_size: 1319905253
  dataset_size: 3052201469
- config_name: 20230601.arc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 830073
    num_examples: 1925
  download_size: 360590
  dataset_size: 830073
- config_name: 20230601.ary
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10007364
    num_examples: 6703
  download_size: 4094420
  dataset_size: 10007364
- config_name: 20230601.arz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1364641408
    num_examples: 1617770
  download_size: 306336320
  dataset_size: 1364641408
- config_name: 20230601.as
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 86645223
    num_examples: 11988
  download_size: 33149841
  dataset_size: 86645223
- config_name: 20230601.ast
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 470349731
    num_examples: 132550
  download_size: 271011784
  dataset_size: 470349731
- config_name: 20230601.atj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 993287
    num_examples: 1965
  download_size: 502890
  dataset_size: 993287
- config_name: 20230601.av
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5996158
    num_examples: 3392
  download_size: 2514243
  dataset_size: 5996158
- config_name: 20230601.avk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 31189461
    num_examples: 27493
  download_size: 7729144
  dataset_size: 31189461
- config_name: 20230601.awa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3588050
    num_examples: 3701
  download_size: 1230725
  dataset_size: 3588050
- config_name: 20230601.ay
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4357283
    num_examples: 5287
  download_size: 1736571
  dataset_size: 4357283
- config_name: 20230601.az
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 432954620
    num_examples: 194486
  download_size: 228131005
  dataset_size: 432954620
- config_name: 20230601.azb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 186034971
    num_examples: 243041
  download_size: 46251265
  dataset_size: 186034971
- config_name: 20230601.ba
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 293142247
    num_examples: 62907
  download_size: 120320323
  dataset_size: 293142247
- config_name: 20230601.ban
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16509353
    num_examples: 19293
  download_size: 6302437
  dataset_size: 16509353
- config_name: 20230601.bar
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36001708
    num_examples: 26978
  download_size: 21611902
  dataset_size: 36001708
- config_name: 20230601.bat-smg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7536614
    num_examples: 17181
  download_size: 3411835
  dataset_size: 7536614
- config_name: 20230601.be-x-old
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 244894736
    num_examples: 82917
  download_size: 110733701
  dataset_size: 244894736
- config_name: 20230601.bcl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18259970
    num_examples: 13934
  download_size: 10086356
  dataset_size: 18259970
- config_name: 20230601.be
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 606416485
    num_examples: 231617
  download_size: 280474552
  dataset_size: 606416485
- config_name: 20230601.bg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1080390968
    num_examples: 291361
  download_size: 506945262
  dataset_size: 1080390968
- config_name: 20230601.bh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16078510
    num_examples: 8446
  download_size: 5648960
  dataset_size: 16078510
- config_name: 20230601.bi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 398357
    num_examples: 1539
  download_size: 200277
  dataset_size: 398357
- config_name: 20230601.bjn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6755874
    num_examples: 10379
  download_size: 3265979
  dataset_size: 6755874
- config_name: 20230601.blk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24413622
    num_examples: 2725
  download_size: 7356285
  dataset_size: 24413622
- config_name: 20230601.bm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 473185
    num_examples: 1221
  download_size: 261438
  dataset_size: 473185
- config_name: 20230601.bn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 913676298
    num_examples: 138515
  download_size: 330147337
  dataset_size: 913676298
- config_name: 20230601.bo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 132034426
    num_examples: 12434
  download_size: 38687191
  dataset_size: 132034426
- config_name: 20230601.bpy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42862119
    num_examples: 25167
  download_size: 6532133
  dataset_size: 42862119
- config_name: 20230601.br
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 84044684
    num_examples: 79959
  download_size: 48952223
  dataset_size: 84044684
- config_name: 20230601.bs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 190816695
    num_examples: 92065
  download_size: 106053913
  dataset_size: 190816695
- config_name: 20230601.bug
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3433134
    num_examples: 15873
  download_size: 815878
  dataset_size: 3433134
- config_name: 20230601.bxr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6695205
    num_examples: 2791
  download_size: 3078381
  dataset_size: 6695205
- config_name: 20230601.ca
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1918941844
    num_examples: 728483
  download_size: 1113762234
  dataset_size: 1918941844
- config_name: 20230601.cbk-zam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2808337
    num_examples: 3307
  download_size: 1261855
  dataset_size: 2808337
- config_name: 20230601.cdo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5010639
    num_examples: 16234
  download_size: 1949302
  dataset_size: 5010639
- config_name: 20230601.ce
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 726468413
    num_examples: 599863
  download_size: 86627608
  dataset_size: 726468413
- config_name: 20230601.ceb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4717690463
    num_examples: 6124009
  download_size: 938189255
  dataset_size: 4717690463
- config_name: 20230601.ch
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 187255
    num_examples: 573
  download_size: 96403
  dataset_size: 187255
- config_name: 20230601.cho
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7974
    num_examples: 14
  download_size: 9782
  dataset_size: 7974
- config_name: 20230601.chr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 764388
    num_examples: 1113
  download_size: 341232
  dataset_size: 764388
- config_name: 20230601.chy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 149009
    num_examples: 801
  download_size: 76580
  dataset_size: 149009
- config_name: 20230601.ckb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 101248717
    num_examples: 49928
  download_size: 40379289
  dataset_size: 101248717
- config_name: 20230601.co
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8069524
    num_examples: 6565
  download_size: 4650142
  dataset_size: 8069524
- config_name: 20230601.cr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 50625
    num_examples: 182
  download_size: 26509
  dataset_size: 50625
- config_name: 20230601.crh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9056373
    num_examples: 25642
  download_size: 3453399
  dataset_size: 9056373
- config_name: 20230601.cs
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1529727976
    num_examples: 525205
  download_size: 966856046
  dataset_size: 1529727976
- config_name: 20230601.csb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3739371
    num_examples: 5478
  download_size: 2049003
  dataset_size: 3739371
- config_name: 20230601.cu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 975765
    num_examples: 1221
  download_size: 395563
  dataset_size: 975765
- config_name: 20230601.cv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 81019358
    num_examples: 51407
  download_size: 29189010
  dataset_size: 81019358
- config_name: 20230601.cy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 304314230
    num_examples: 278927
  download_size: 111093453
  dataset_size: 304314230
- config_name: 20230601.da
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 540186121
    num_examples: 291721
  download_size: 326825586
  dataset_size: 540186121
- config_name: 20230601.dag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8116697
    num_examples: 8850
  download_size: 3469680
  dataset_size: 8116697
- config_name: 20230601.de
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9446726072
    num_examples: 2801769
  download_size: 5752429951
  dataset_size: 9446726072
- config_name: 20230601.din
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 554422
    num_examples: 506
  download_size: 334229
  dataset_size: 554422
- config_name: 20230601.diq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19300910
    num_examples: 40589
  download_size: 7469118
  dataset_size: 19300910
- config_name: 20230601.dsb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3303132
    num_examples: 3357
  download_size: 1923763
  dataset_size: 3303132
- config_name: 20230601.dty
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6972841
    num_examples: 3625
  download_size: 2497168
  dataset_size: 6972841
- config_name: 20230601.dv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13916007
    num_examples: 4344
  download_size: 5255070
  dataset_size: 13916007
- config_name: 20230601.dz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8517069
    num_examples: 777
  download_size: 2474869
  dataset_size: 8517069
- config_name: 20230601.ee
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 844062
    num_examples: 1164
  download_size: 464418
  dataset_size: 844062
- config_name: 20230601.el
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1314451459
    num_examples: 222598
  download_size: 627997252
  dataset_size: 1314451459
- config_name: 20230601.eml
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3605037
    num_examples: 12945
  download_size: 1681847
  dataset_size: 3605037
- config_name: 20230601.en
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21325670826
    num_examples: 6660918
  download_size: 12512970849
  dataset_size: 21325670826
- config_name: 20230601.eo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 508055613
    num_examples: 337291
  download_size: 294377264
  dataset_size: 508055613
- config_name: 20230601.es
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5889963046
    num_examples: 1805012
  download_size: 3477902737
  dataset_size: 5889963046
- config_name: 20230601.eu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 547125100
    num_examples: 405840
  download_size: 264099434
  dataset_size: 547125100
- config_name: 20230601.ext
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4182030
    num_examples: 3636
  download_size: 2631658
  dataset_size: 4182030
- config_name: 20230601.fa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1851617207
    num_examples: 964236
  download_size: 759372155
  dataset_size: 1851617207
- config_name: 20230601.fat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1933259
    num_examples: 1046
  download_size: 1067434
  dataset_size: 1933259
- config_name: 20230601.ff
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1401981
    num_examples: 1484
  download_size: 824781
  dataset_size: 1401981
- config_name: 20230601.fi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1125659121
    num_examples: 553519
  download_size: 678674705
  dataset_size: 1125659121
- config_name: 20230601.fiu-vro
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4773469
    num_examples: 6559
  download_size: 2464729
  dataset_size: 4773469
- config_name: 20230601.fj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 593373
    num_examples: 1283
  download_size: 323108
  dataset_size: 593373
- config_name: 20230601.fo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15058635
    num_examples: 13954
  download_size: 8633381
  dataset_size: 15058635
- config_name: 20230601.fr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7910192478
    num_examples: 2525926
  download_size: 4618774275
  dataset_size: 7910192478
- config_name: 20230601.frp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3517265
    num_examples: 5689
  download_size: 1847765
  dataset_size: 3517265
- config_name: 20230601.frr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10292357
    num_examples: 17260
  download_size: 5084999
  dataset_size: 10292357
- config_name: 20230601.fur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4062291
    num_examples: 3967
  download_size: 2401534
  dataset_size: 4062291
- config_name: 20230601.fy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 130189677
    num_examples: 51506
  download_size: 73624821
  dataset_size: 130189677
- config_name: 20230601.ga
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 59266973
    num_examples: 58579
  download_size: 33377343
  dataset_size: 59266973
- config_name: 20230601.gag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2405210
    num_examples: 2966
  download_size: 1319553
  dataset_size: 2405210
- config_name: 20230601.gan
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2878337
    num_examples: 6691
  download_size: 1485195
  dataset_size: 2878337
- config_name: 20230601.gcr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2335924
    num_examples: 2397
  download_size: 1344338
  dataset_size: 2335924
- config_name: 20230601.gd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14026914
    num_examples: 16018
  download_size: 7175920
  dataset_size: 14026914
- config_name: 20230601.gl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 483432936
    num_examples: 196473
  download_size: 287329100
  dataset_size: 483432936
- config_name: 20230601.glk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6067898
    num_examples: 7035
  download_size: 2372761
  dataset_size: 6067898
- config_name: 20230601.gn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6754303
    num_examples: 5298
  download_size: 3702975
  dataset_size: 6754303
- config_name: 20230601.gom
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 30830020
    num_examples: 4250
  download_size: 11258918
  dataset_size: 30830020
- config_name: 20230601.gor
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6111487
    num_examples: 14556
  download_size: 2036928
  dataset_size: 6111487
- config_name: 20230601.got
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1518930
    num_examples: 1005
  download_size: 626840
  dataset_size: 1518930
- config_name: 20230601.gu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 120869564
    num_examples: 30357
  download_size: 39339802
  dataset_size: 120869564
- config_name: 20230601.guc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 916033
    num_examples: 578
  download_size: 547551
  dataset_size: 916033
- config_name: 20230601.gur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1414225
    num_examples: 954
  download_size: 753483
  dataset_size: 1414225
- config_name: 20230601.guw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1894278
    num_examples: 1301
  download_size: 1027313
  dataset_size: 1894278
- config_name: 20230601.gv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5969707
    num_examples: 5954
  download_size: 3155779
  dataset_size: 5969707
- config_name: 20230601.ha
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 62945985
    num_examples: 27905
  download_size: 35159511
  dataset_size: 62945985
- config_name: 20230601.hak
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4493017
    num_examples: 10183
  download_size: 1875697
  dataset_size: 4493017
- config_name: 20230601.haw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1648045
    num_examples: 2580
  download_size: 681202
  dataset_size: 1648045
- config_name: 20230601.he
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1890961532
    num_examples: 325534
  download_size: 955373507
  dataset_size: 1890961532
- config_name: 20230601.hi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 652930384
    num_examples: 160068
  download_size: 230339569
  dataset_size: 652930384
- config_name: 20230601.hif
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5670768
    num_examples: 10975
  download_size: 2708959
  dataset_size: 5670768
- config_name: 20230601.ho
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3450
    num_examples: 3
  download_size: 7714
  dataset_size: 3450
- config_name: 20230601.hsb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 15650862
    num_examples: 13929
  download_size: 7422054
  dataset_size: 15650862
- config_name: 20230601.ht
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 54468681
    num_examples: 69778
  download_size: 21591458
  dataset_size: 54468681
- config_name: 20230601.hu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1490296647
    num_examples: 526030
  download_size: 904279478
  dataset_size: 1490296647
- config_name: 20230601.hy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1142467643
    num_examples: 297933
  download_size: 477398053
  dataset_size: 1142467643
- config_name: 20230601.hyw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 57478946
    num_examples: 10933
  download_size: 26499417
  dataset_size: 57478946
- config_name: 20230601.ia
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16183963
    num_examples: 27939
  download_size: 8108662
  dataset_size: 16183963
- config_name: 20230601.id
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1086885042
    num_examples: 648383
  download_size: 575124507
  dataset_size: 1086885042
- config_name: 20230601.ie
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6482834
    num_examples: 11705
  download_size: 2881031
  dataset_size: 6482834
- config_name: 20230601.ig
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 45043729
    num_examples: 16970
  download_size: 23565907
  dataset_size: 45043729
- config_name: 20230601.ii
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8921
    num_examples: 14
  download_size: 14936
  dataset_size: 8921
- config_name: 20230601.ik
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 190236
    num_examples: 823
  download_size: 109460
  dataset_size: 190236
- config_name: 20230601.ilo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16860855
    num_examples: 15379
  download_size: 7350161
  dataset_size: 16860855
- config_name: 20230601.inh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2697943
    num_examples: 2108
  download_size: 1257824
  dataset_size: 2697943
- config_name: 20230601.io
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37291268
    num_examples: 38155
  download_size: 16629067
  dataset_size: 37291268
- config_name: 20230601.is
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 86487184
    num_examples: 56795
  download_size: 51372350
  dataset_size: 86487184
- config_name: 20230601.it
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4826403309
    num_examples: 1812514
  download_size: 2926177870
  dataset_size: 4826403309
- config_name: 20230601.iu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 284349
    num_examples: 564
  download_size: 132368
  dataset_size: 284349
- config_name: 20230601.ja
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6913216645
    num_examples: 1373311
  download_size: 3923535785
  dataset_size: 6913216645
- config_name: 20230601.jam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1140551
    num_examples: 1771
  download_size: 700995
  dataset_size: 1140551
- config_name: 20230601.jbo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2521508
    num_examples: 1390
  download_size: 888087
  dataset_size: 2521508
- config_name: 20230601.jv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 70703094
    num_examples: 73024
  download_size: 36199167
  dataset_size: 70703094
- config_name: 20230601.ka
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 693108151
    num_examples: 168185
  download_size: 237719175
  dataset_size: 693108151
- config_name: 20230601.kaa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4584133
    num_examples: 3560
  download_size: 2620141
  dataset_size: 4584133
- config_name: 20230601.kab
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4374017
    num_examples: 5800
  download_size: 2570505
  dataset_size: 4374017
- config_name: 20230601.kbd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3034249
    num_examples: 1637
  download_size: 1317388
  dataset_size: 3034249
- config_name: 20230601.kbp
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3571606
    num_examples: 1918
  download_size: 1794790
  dataset_size: 3571606
- config_name: 20230601.kcg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 663326
    num_examples: 825
  download_size: 350587
  dataset_size: 663326
- config_name: 20230601.kg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 463083
    num_examples: 1333
  download_size: 240321
  dataset_size: 463083
- config_name: 20230601.ki
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 453178
    num_examples: 1635
  download_size: 243544
  dataset_size: 453178
- config_name: 20230601.kj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5190
    num_examples: 5
  download_size: 10453
  dataset_size: 5190
- config_name: 20230601.kk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 488955469
    num_examples: 237304
  download_size: 176872369
  dataset_size: 488955469
- config_name: 20230601.kl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 312839
    num_examples: 298
  download_size: 193192
  dataset_size: 312839
- config_name: 20230601.km
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 102051337
    num_examples: 11784
  download_size: 35067125
  dataset_size: 102051337
- config_name: 20230601.kn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 394061570
    num_examples: 30793
  download_size: 143867617
  dataset_size: 394061570
- config_name: 20230601.ko
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1374136790
    num_examples: 635278
  download_size: 777760206
  dataset_size: 1374136790
- config_name: 20230601.koi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5077608
    num_examples: 3487
  download_size: 1880469
  dataset_size: 5077608
- config_name: 20230601.krc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4592333
    num_examples: 2098
  download_size: 2019043
  dataset_size: 4592333
- config_name: 20230601.ks
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2380920
    num_examples: 4060
  download_size: 849849
  dataset_size: 2380920
- config_name: 20230601.ksh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3110398
    num_examples: 2945
  download_size: 2004743
  dataset_size: 3110398
- config_name: 20230601.ku
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42327613
    num_examples: 59529
  download_size: 21970440
  dataset_size: 42327613
- config_name: 20230601.kv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9221030
    num_examples: 5589
  download_size: 3676356
  dataset_size: 9221030
- config_name: 20230601.kw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4653320
    num_examples: 7070
  download_size: 2695687
  dataset_size: 4653320
- config_name: 20230601.ky
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 168214006
    num_examples: 80594
  download_size: 64353836
  dataset_size: 168214006
- config_name: 20230601.la
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 139977277
    num_examples: 137851
  download_size: 75850224
  dataset_size: 139977277
- config_name: 20230601.lad
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4820385
    num_examples: 3638
  download_size: 2703040
  dataset_size: 4820385
- config_name: 20230601.lb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 87567860
    num_examples: 61757
  download_size: 49791518
  dataset_size: 87567860
- config_name: 20230601.lbe
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 698292
    num_examples: 1276
  download_size: 282486
  dataset_size: 698292
- config_name: 20230601.lez
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9785097
    num_examples: 4256
  download_size: 3849506
  dataset_size: 9785097
- config_name: 20230601.lfn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8850905
    num_examples: 4805
  download_size: 5189938
  dataset_size: 8850905
- config_name: 20230601.lg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6771716
    num_examples: 4016
  download_size: 3634293
  dataset_size: 6771716
- config_name: 20230601.li
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 29183994
    num_examples: 14308
  download_size: 17566220
  dataset_size: 29183994
- config_name: 20230601.lij
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11088927
    num_examples: 11132
  download_size: 6042920
  dataset_size: 11088927
- config_name: 20230601.lld
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 45325217
    num_examples: 158242
  download_size: 12436563
  dataset_size: 45325217
- config_name: 20230601.lmo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 42267433
    num_examples: 71061
  download_size: 18724770
  dataset_size: 42267433
- config_name: 20230601.ln
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2024697
    num_examples: 3515
  download_size: 1115171
  dataset_size: 2024697
- config_name: 20230601.lo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14729412
    num_examples: 4928
  download_size: 5382036
  dataset_size: 14729412
- config_name: 20230601.lrc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 144
    num_examples: 1
  download_size: 2723
  dataset_size: 144
- config_name: 20230601.lt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 331252602
    num_examples: 208114
  download_size: 191925990
  dataset_size: 331252602
- config_name: 20230601.ltg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 901980
    num_examples: 1044
  download_size: 522213
  dataset_size: 901980
- config_name: 20230601.lv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 220969643
    num_examples: 120295
  download_size: 126161867
  dataset_size: 220969643
- config_name: 20230601.mad
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1325061
    num_examples: 1103
  download_size: 764579
  dataset_size: 1325061
- config_name: 20230601.mai
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21215977
    num_examples: 14622
  download_size: 6041134
  dataset_size: 21215977
- config_name: 20230601.map-bms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5400186
    num_examples: 13554
  download_size: 2420169
  dataset_size: 5400186
- config_name: 20230601.mdf
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4033455
    num_examples: 3473
  download_size: 1513534
  dataset_size: 4033455
- config_name: 20230601.mg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71936817
    num_examples: 95675
  download_size: 21206762
  dataset_size: 71936817
- config_name: 20230601.mh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11524
    num_examples: 8
  download_size: 16877
  dataset_size: 11524
- config_name: 20230601.mhr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19030836
    num_examples: 11016
  download_size: 6821706
  dataset_size: 19030836
- config_name: 20230601.mi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4120867
    num_examples: 7855
  download_size: 1016905
  dataset_size: 4120867
- config_name: 20230601.min
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 118484114
    num_examples: 226953
  download_size: 25401691
  dataset_size: 118484114
- config_name: 20230601.mk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 633734922
    num_examples: 136723
  download_size: 263383509
  dataset_size: 633734922
- config_name: 20230601.ml
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 485143578
    num_examples: 84794
  download_size: 179727029
  dataset_size: 485143578
- config_name: 20230601.mn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 88813927
    num_examples: 23385
  download_size: 40026827
  dataset_size: 88813927
- config_name: 20230601.mni
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9790220
    num_examples: 10877
  download_size: 2193774
  dataset_size: 9790220
- config_name: 20230601.mnw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 45579901
    num_examples: 3184
  download_size: 13207357
  dataset_size: 45579901
- config_name: 20230601.mr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 254646708
    num_examples: 92898
  download_size: 79982313
  dataset_size: 254646708
- config_name: 20230601.mrj
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8729899
    num_examples: 10542
  download_size: 3278742
  dataset_size: 8729899
- config_name: 20230601.ms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 410354637
    num_examples: 365491
  download_size: 206610861
  dataset_size: 410354637
- config_name: 20230601.mt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 26613613
    num_examples: 5369
  download_size: 15563924
  dataset_size: 26613613
- config_name: 20230601.mus
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 922
    num_examples: 2
  download_size: 5286
  dataset_size: 922
- config_name: 20230601.mwl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 19284605
    num_examples: 4474
  download_size: 11469001
  dataset_size: 19284605
- config_name: 20230601.my
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 310836677
    num_examples: 108750
  download_size: 84350660
  dataset_size: 310836677
- config_name: 20230601.myv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11073788
    num_examples: 7910
  download_size: 4560227
  dataset_size: 11073788
- config_name: 20230601.mzn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14682517
    num_examples: 15995
  download_size: 4856126
  dataset_size: 14682517
- config_name: 20230601.nah
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2843124
    num_examples: 6654
  download_size: 1347633
  dataset_size: 2843124
- config_name: 20230601.nap
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6365024
    num_examples: 14849
  download_size: 3169570
  dataset_size: 6365024
- config_name: 20230601.nds
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 92743798
    num_examples: 84225
  download_size: 47925882
  dataset_size: 92743798
- config_name: 20230601.nds-nl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 13432115
    num_examples: 7669
  download_size: 8207550
  dataset_size: 13432115
- config_name: 20230601.ne
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 105562688
    num_examples: 32084
  download_size: 36335987
  dataset_size: 105562688
- config_name: 20230601.new
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159067466
    num_examples: 73004
  download_size: 20472096
  dataset_size: 159067466
- config_name: 20230601.ng
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 68090
    num_examples: 21
  download_size: 52355
  dataset_size: 68090
- config_name: 20230601.nia
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1793045
    num_examples: 1638
  download_size: 908004
  dataset_size: 1793045
- config_name: 20230601.nl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2607286503
    num_examples: 2123556
  download_size: 1451716829
  dataset_size: 2607286503
- config_name: 20230601.nn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 233905017
    num_examples: 165610
  download_size: 132674509
  dataset_size: 233905017
- config_name: 20230601.no
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1018553680
    num_examples: 611542
  download_size: 594771430
  dataset_size: 1018553680
- config_name: 20230601.nov
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 912652
    num_examples: 1626
  download_size: 466451
  dataset_size: 912652
- config_name: 20230601.nqo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8295905
    num_examples: 1577
  download_size: 3503359
  dataset_size: 8295905
- config_name: 20230601.nrm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3212495
    num_examples: 4887
  download_size: 1504411
  dataset_size: 3212495
- config_name: 20230601.nso
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2753446
    num_examples: 8617
  download_size: 912548
  dataset_size: 2753446
- config_name: 20230601.nv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16785014
    num_examples: 22189
  download_size: 3271175
  dataset_size: 16785014
- config_name: 20230601.ny
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1693443
    num_examples: 1133
  download_size: 937213
  dataset_size: 1693443
- config_name: 20230601.oc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 117818984
    num_examples: 88886
  download_size: 62764519
  dataset_size: 117818984
- config_name: 20230601.olo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3122448
    num_examples: 4514
  download_size: 1707016
  dataset_size: 3122448
- config_name: 20230601.om
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3057811
    num_examples: 1574
  download_size: 1720686
  dataset_size: 3057811
- config_name: 20230601.or
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71342568
    num_examples: 16793
  download_size: 25347488
  dataset_size: 71342568
- config_name: 20230601.os
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12975022
    num_examples: 17066
  download_size: 5519425
  dataset_size: 12975022
- config_name: 20230601.pa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 205173613
    num_examples: 49955
  download_size: 78370120
  dataset_size: 205173613
- config_name: 20230601.pag
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1336264
    num_examples: 2638
  download_size: 417192
  dataset_size: 1336264
- config_name: 20230601.pam
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8241795
    num_examples: 8935
  download_size: 4231831
  dataset_size: 8241795
- config_name: 20230601.pap
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3662048
    num_examples: 3237
  download_size: 2098802
  dataset_size: 3662048
- config_name: 20230601.pcd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5622299
    num_examples: 5639
  download_size: 3094652
  dataset_size: 5622299
- config_name: 20230601.pcm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1531576
    num_examples: 954
  download_size: 937573
  dataset_size: 1531576
- config_name: 20230601.pdc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1196915
    num_examples: 2162
  download_size: 688667
  dataset_size: 1196915
- config_name: 20230601.pfl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3682829
    num_examples: 2756
  download_size: 1962515
  dataset_size: 3682829
- config_name: 20230601.pi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1134003
    num_examples: 3056
  download_size: 196632
  dataset_size: 1134003
- config_name: 20230601.pih
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 378374
    num_examples: 930
  download_size: 236668
  dataset_size: 378374
- config_name: 20230601.pl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2904184909
    num_examples: 1569515
  download_size: 1787531053
  dataset_size: 2904184909
- config_name: 20230601.pms
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 34301415
    num_examples: 67899
  download_size: 11986805
  dataset_size: 34301415
- config_name: 20230601.pnb
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 298316454
    num_examples: 70562
  download_size: 130650981
  dataset_size: 298316454
- config_name: 20230601.pnt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 675000
    num_examples: 535
  download_size: 298222
  dataset_size: 675000
- config_name: 20230601.ps
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 104012780
    num_examples: 19565
  download_size: 48710783
  dataset_size: 104012780
- config_name: 20230601.pt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2693736720
    num_examples: 1103446
  download_size: 1571347957
  dataset_size: 2693736720
- config_name: 20230601.pwn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 800565
    num_examples: 380
  download_size: 446595
  dataset_size: 800565
- config_name: 20230601.qu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 16631588
    num_examples: 23909
  download_size: 7575996
  dataset_size: 16631588
- config_name: 20230601.rm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 17822525
    num_examples: 3815
  download_size: 10339459
  dataset_size: 17822525
- config_name: 20230601.rmy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 491195
    num_examples: 930
  download_size: 285442
  dataset_size: 491195
- config_name: 20230601.rn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 522745
    num_examples: 805
  download_size: 295575
  dataset_size: 522745
- config_name: 20230601.ro
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 834681972
    num_examples: 440015
  download_size: 466488330
  dataset_size: 834681972
- config_name: 20230601.roa-rup
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1713384
    num_examples: 1409
  download_size: 955926
  dataset_size: 1713384
- config_name: 20230601.roa-tara
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 7418561
    num_examples: 9337
  download_size: 3970663
  dataset_size: 7418561
- config_name: 20230601.ru
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10097718899
    num_examples: 1918942
  download_size: 4880008552
  dataset_size: 10097718899
- config_name: 20230601.rue
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12975836
    num_examples: 8703
  download_size: 6269020
  dataset_size: 12975836
- config_name: 20230601.rw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10794817
    num_examples: 7425
  download_size: 6009979
  dataset_size: 10794817
- config_name: 20230601.sa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 69233233
    num_examples: 12101
  download_size: 23590461
  dataset_size: 69233233
- config_name: 20230601.sah
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 47530889
    num_examples: 16598
  download_size: 21213858
  dataset_size: 47530889
- config_name: 20230601.sat
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 35005528
    num_examples: 8264
  download_size: 12124520
  dataset_size: 35005528
- config_name: 20230601.sc
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12683528
    num_examples: 7540
  download_size: 7650423
  dataset_size: 12683528
- config_name: 20230601.scn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 17672274
    num_examples: 26507
  download_size: 10210177
  dataset_size: 17672274
- config_name: 20230601.sco
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 43796852
    num_examples: 36206
  download_size: 24764727
  dataset_size: 43796852
- config_name: 20230601.sd
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36672141
    num_examples: 16882
  download_size: 17409382
  dataset_size: 36672141
- config_name: 20230601.se
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3600247
    num_examples: 8040
  download_size: 1814982
  dataset_size: 3600247
- config_name: 20230601.sg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 127791
    num_examples: 548
  download_size: 63800
  dataset_size: 127791
- config_name: 20230601.sh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 569915575
    num_examples: 458272
  download_size: 270502498
  dataset_size: 569915575
- config_name: 20230601.shi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2195129
    num_examples: 1544
  download_size: 1311300
  dataset_size: 2195129
- config_name: 20230601.shn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 33233508
    num_examples: 13706
  download_size: 8107005
  dataset_size: 33233508
- config_name: 20230601.si
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 135560965
    num_examples: 22574
  download_size: 52870973
  dataset_size: 135560965
- config_name: 20230601.sk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 410287543
    num_examples: 240597
  download_size: 237984111
  dataset_size: 410287543
- config_name: 20230601.skr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 22294235
    num_examples: 5739
  download_size: 9744982
  dataset_size: 22294235
- config_name: 20230601.sl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 444732062
    num_examples: 181212
  download_size: 263697513
  dataset_size: 444732062
- config_name: 20230601.sm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 891597
    num_examples: 1143
  download_size: 485815
  dataset_size: 891597
- config_name: 20230601.smn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5526668
    num_examples: 5094
  download_size: 2710998
  dataset_size: 5526668
- config_name: 20230601.sn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9252554
    num_examples: 10917
  download_size: 4738498
  dataset_size: 9252554
- config_name: 20230601.so
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14893759
    num_examples: 10812
  download_size: 8617659
  dataset_size: 14893759
- config_name: 20230601.sq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 197206847
    num_examples: 100423
  download_size: 110414776
  dataset_size: 197206847
- config_name: 20230601.sr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1690745100
    num_examples: 671352
  download_size: 695586988
  dataset_size: 1690745100
- config_name: 20230601.srn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 649044
    num_examples: 1218
  download_size: 214987
  dataset_size: 649044
- config_name: 20230601.ss
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 861417
    num_examples: 720
  download_size: 489383
  dataset_size: 861417
- config_name: 20230601.st
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 934954
    num_examples: 1073
  download_size: 517491
  dataset_size: 934954
- config_name: 20230601.stq
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4929355
    num_examples: 4129
  download_size: 2878034
  dataset_size: 4929355
- config_name: 20230601.su
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 47909002
    num_examples: 61490
  download_size: 19683635
  dataset_size: 47909002
- config_name: 20230601.sv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2133848723
    num_examples: 2564263
  download_size: 1002020509
  dataset_size: 2133848723
- config_name: 20230601.sw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 71857907
    num_examples: 77334
  download_size: 35252918
  dataset_size: 71857907
- config_name: 20230601.szl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21335080
    num_examples: 56652
  download_size: 7284436
  dataset_size: 21335080
- config_name: 20230601.szy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10412319
    num_examples: 4709
  download_size: 5572825
  dataset_size: 10412319
- config_name: 20230601.tay
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2779734
    num_examples: 2595
  download_size: 1147869
  dataset_size: 2779734
- config_name: 20230601.tcy
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11968976
    num_examples: 2173
  download_size: 4524692
  dataset_size: 11968976
- config_name: 20230601.te
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 705766405
    num_examples: 83107
  download_size: 206360536
  dataset_size: 705766405
- config_name: 20230601.tet
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1457614
    num_examples: 1460
  download_size: 739227
  dataset_size: 1457614
- config_name: 20230601.tg
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 145506377
    num_examples: 109839
  download_size: 48637192
  dataset_size: 145506377
- config_name: 20230601.th
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 987873133
    num_examples: 156445
  download_size: 365894157
  dataset_size: 987873133
- config_name: 20230601.ti
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 665363
    num_examples: 433
  download_size: 328037
  dataset_size: 665363
- config_name: 20230601.tk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 12580480
    num_examples: 7836
  download_size: 6951103
  dataset_size: 12580480
- config_name: 20230601.tl
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 82731267
    num_examples: 44797
  download_size: 44058126
  dataset_size: 82731267
- config_name: 20230601.tn
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3562981
    num_examples: 1162
  download_size: 1244173
  dataset_size: 3562981
- config_name: 20230601.to
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1074947
    num_examples: 1848
  download_size: 510687
  dataset_size: 1074947
- config_name: 20230601.tpi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 450891
    num_examples: 1390
  download_size: 236441
  dataset_size: 450891
- config_name: 20230601.tr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 965186144
    num_examples: 524184
  download_size: 543958666
  dataset_size: 965186144
- config_name: 20230601.trv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4873244
    num_examples: 1809
  download_size: 2635461
  dataset_size: 4873244
- config_name: 20230601.ts
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 841497
    num_examples: 769
  download_size: 451958
  dataset_size: 841497
- config_name: 20230601.tt
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 679276199
    num_examples: 500608
  download_size: 128386602
  dataset_size: 679276199
- config_name: 20230601.tum
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 8395079
    num_examples: 14169
  download_size: 3225881
  dataset_size: 8395079
- config_name: 20230601.tw
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6562128
    num_examples: 3608
  download_size: 3389042
  dataset_size: 6562128
- config_name: 20230601.ty
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 324678
    num_examples: 1348
  download_size: 145184
  dataset_size: 324678
- config_name: 20230601.tyv
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14032235
    num_examples: 3459
  download_size: 6378954
  dataset_size: 14032235
- config_name: 20230601.udm
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6918258
    num_examples: 5586
  download_size: 2937644
  dataset_size: 6918258
- config_name: 20230601.ug
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 41939834
    num_examples: 8557
  download_size: 17588763
  dataset_size: 41939834
- config_name: 20230601.uk
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 4815765166
    num_examples: 1266287
  download_size: 2257591520
  dataset_size: 4815765166
- config_name: 20230601.ur
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 394375073
    num_examples: 194435
  download_size: 160552761
  dataset_size: 394375073
- config_name: 20230601.uz
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 372775375
    num_examples: 241353
  download_size: 196367714
  dataset_size: 372775375
- config_name: 20230601.ve
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 347015
    num_examples: 836
  download_size: 159547
  dataset_size: 347015
- config_name: 20230601.vec
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 37671800
    num_examples: 69181
  download_size: 16029908
  dataset_size: 37671800
- config_name: 20230601.vep
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11259222
    num_examples: 6851
  download_size: 6196150
  dataset_size: 11259222
- config_name: 20230601.vi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1584847634
    num_examples: 1283785
  download_size: 731354374
  dataset_size: 1584847634
- config_name: 20230601.vls
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11296047
    num_examples: 7824
  download_size: 6952370
  dataset_size: 11296047
- config_name: 20230601.vo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18943004
    num_examples: 33641
  download_size: 6379410
  dataset_size: 18943004
- config_name: 20230601.wa
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 11990482
    num_examples: 11858
  download_size: 7144929
  dataset_size: 11990482
- config_name: 20230601.war
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 468715357
    num_examples: 1266238
  download_size: 109807953
  dataset_size: 468715357
- config_name: 20230601.wo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 3498671
    num_examples: 1719
  download_size: 2076485
  dataset_size: 3498671
- config_name: 20230601.wuu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 24986530
    num_examples: 42950
  download_size: 15960262
  dataset_size: 24986530
- config_name: 20230601.xal
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1386014
    num_examples: 2307
  download_size: 508481
  dataset_size: 1386014
- config_name: 20230601.xh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2320277
    num_examples: 1601
  download_size: 1444732
  dataset_size: 2320277
- config_name: 20230601.xmf
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36557690
    num_examples: 17705
  download_size: 12535173
  dataset_size: 36557690
- config_name: 20230601.yi
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 36031133
    num_examples: 15297
  download_size: 16153644
  dataset_size: 36031133
- config_name: 20230601.yo
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 18018480
    num_examples: 33179
  download_size: 8274108
  dataset_size: 18018480
- config_name: 20230601.za
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1276590
    num_examples: 2722
  download_size: 642448
  dataset_size: 1276590
- config_name: 20230601.zea
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 5059421
    num_examples: 5756
  download_size: 2547904
  dataset_size: 5059421
- config_name: 20230601.zh
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2720688196
    num_examples: 1357881
  download_size: 1718953037
  dataset_size: 2720688196
- config_name: 20230601.zh-classical
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 14617535
    num_examples: 12513
  download_size: 9882532
  dataset_size: 14617535
- config_name: 20230601.zh-min-nan
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 159218053
    num_examples: 432531
  download_size: 37371610
  dataset_size: 159218053
- config_name: 20230601.zh-yue
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 107325669
    num_examples: 131542
  download_size: 63294114
  dataset_size: 107325669
- config_name: 20230601.zu
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 6915666
    num_examples: 11381
  download_size: 3683813
  dataset_size: 6915666
- config_name: 20230601.hr
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 448338371
    num_examples: 200748
  download_size: 279406863
  dataset_size: 448338371
- config_name: 20230601.simple
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 282844880
    num_examples: 231233
  download_size: 154520600
  dataset_size: 282844880
- config_name: 20230601.ta
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 803137068
    num_examples: 156273
  download_size: 261269512
  dataset_size: 803137068
---

# Wikipedia

This Wikipedia dataset contains all available languages for recent dumps. It is
a refresh of the [20220301 wikipedia](https://hf.co/datasets/wikipedia) from
Huggingface, so it has the same license and dataset card details. The benefits
of this dataset are:

- more recent dumps (see table below)
- a few additional languages
- all available languages are preprocessed (including the largests: `en` and
  `ceb`)

| version | dump     | # available languages   | closed & dump                                   | closed & no dump  |
| -----   | ----     | -----                   | ------                                          | ---               |
| `1.0.0` | 20230601 | 328                     | 9: ak (soon), cho, ho, ii, kj, lrc, mh, mus, ng | 4: aa, hz, kr, na |
|         | 20230901 | see you in September... |                                                 |                   |

Source: [List of Wikimedia
Languages](https://en.wikipedia.org/wiki/List_of_Wikipedias). A few (9)
Wikimedias are closed, meaning they won't have new pages, but the dumps are
still available. In addition, very few (4) Wikimedias are closed and don't
have dumps anymore.

## Release Notes

`1.0.0`

- **chore**: File layout is now `data/{dump}/{lang}/{info.json,*.parquet}`.
  Sorry for the radical update, probably won't happen again.
- **chore**: Parquet files are now sharded (size < 200 MB), allowing parallel
  downloads and processing.
- **fix**: All languages were all processed again because of a bug in the media
  and category names, leading to some links not being extracted.
- **feat**: Add `en` and `ceb` which were too big for my Beam DirectRunner at
  the time.

## Usage

```python
from datasets import load_dataset

wikipedia_es = load_dataset("graelo/wikipedia", "20230601.es")
```

---

## Build instructions

Developer only. This dataset was preprocessed with a Beam DirectRunner as
follows.

### 1. Determine the date of the dump you are interested in

Choose one wikipedia dump, for instance <https://dumps.wikimedia.org/cewiki/>
and identify the date.

### 2. [Optional] Get a refreshed list of languages

This is optional because it not very likely that a new language will have
suddenly appeared since the last version _and_ have a significant dataset.

Navigate to <https://en.wikipedia.org/wiki/List_of_Wikipedias> and copy the
languages column from the "Detailed list" table (near the end of the page).

Copy that content in the form of a Python list into `lang_def.py` (at the top
of the repo) under a new date.

### 3. [Optional] Create Media and Category aliases

In order to properly extract links to images and media in all languages, we
must refresh the two corresponding files. To do so, from the root of the repo,
run

```sh
python -m prep.create_aliases
```

This will create or update these two files at the root of the repo:

- `media_aliases.py`
- `category_aliases.py`

These files are used in the final step

### 4. Build and prepare the datasets into sharded parquet files

Running this script downloads the wikipedia dumps for each language in
`lang_def.py` and shards each language dataset into the appropriate number of
shards (max size ~ 250MB).

```sh
python -m prep.build --date 20230601
```

There are other options:

```text
$ python -m prep.build --help
usage: Wikipedia Builder [-h] [--date DATE] [--language [LANG ...]] [--cache-dir DIR] [--mirror MIRROR]

Prepares the Wikipedia dataset for each language

optional arguments:
  -h, --help             show this help message and exit
  --date DATE            Wikipedia dump date (e.g. 20230601)
  --language [LANG ...]  Language code (e.g. en). If missing, all languages are processed
  --cache-dir DIR        Cache directory for 🤗 Datasets
  --mirror MIRROR        Mirror URL
```

For instance, for faster downloads of the dumps, use the mirror option:

```sh
python -m prep.build \
    --date 20230601 \
    --language bs \
    --mirror https://mirror.accum.se/mirror/wikimedia.org/dumps/
```

It will download the dumps at around 60MB/s instead of the capped speed
(~4MB/s) from <https://dumps.wikimedia.org>. The script will skip existing
directories, allowing you to run the script in several passes.

Notes:

- These instructions build upon the build process of the
  [Wikipedia](https://huggingface.co/datasets/wikipedia) 🤗 Dataset. HF did a
  fantastic job, I just pushed it a bit further.
- Be aware that not all mirrors contain all dumps. For instance mirror.accum.se
  does not contain dumps for languages such as be-x-old or cbk-zam. My own
  solution is to run a first pass using the aforementioned mirror, and a second
  pass with the official `https://dumps.wikimedia.org` site (omitting the
  `--mirror` parameter).

