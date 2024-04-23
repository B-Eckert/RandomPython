import random
from datetime import datetime
import os

cuneiform = ['𒀀', '𒀁', '𒀂', '𒀃', '𒀄', '𒀅', '𒀆', '𒀇', '𒀈', '𒀉', '𒀊', '𒀋', '𒀌', '𒀍', '𒀎', '𒀏', '𒀐', '𒀑', '𒀒', '𒀓', '𒀔', '𒀕', '𒀖', '𒀗', 
             '𒀘', '𒀙', '𒀚', '𒀛', '𒀜', '𒀝', '𒀞', '𒀟', '𒀠', '𒀡', '𒀢', '𒀣', '𒀤', '𒀥', '𒀦', '𒀧', '𒀨', '𒀩', '𒀪', '𒀫', '𒀬', '𒀭', '𒀮', '𒀯', 
             '𒀰', '𒀱', '𒀲', '𒀳', '𒀴', '𒀵', '𒀶', '𒀷', '𒀸', '𒀹', '𒀺', '𒀻', '𒀼', '𒀽', '𒀾', '𒀿', '𒁀', '𒁁', '𒁂', '𒁃', '𒁄', '𒁅', '𒁆', '𒁇', 
             '𒁈', '𒁉', '𒁊', '𒁋', '𒁌', '𒁍', '𒁎', '𒁏', '𒁐', '𒁑', '𒁒', '𒁓', '𒁔', '𒁕', '𒁖', '𒁗', '𒁘', '𒁙', '𒁚', '𒁛', '𒁜', 
             '𒁝', '𒁞', '𒁟', '𒁠', '𒁡', '𒁢', '𒁣', '𒁤', '𒁥', '𒁦', '𒁧', '𒁨', '𒁩', '𒁪', '𒁫', '𒁬', '𒁭', '𒁮', 
             '𒁯', '𒁰', '𒁱', '𒁲', '𒁳', '𒁴', '𒁵', '𒁶', '𒁷', '𒁸', '𒁹', '𒁺', '𒁻', '𒁼', '𒁽', '𒁾', '𒁿', '𒂀', '𒂁', '𒂂', '𒂃', '𒂄', '𒂅', 
             '𒂆', '𒂇', '𒂈', '𒂉', '𒂊', '𒂋', '𒂌', '𒂍', '𒂎', '𒂏', '𒂐', '𒂑', '𒂒', '𒂓', '𒂔', '𒂕', '𒂖', '𒂗', '𒂘', '𒂙', '𒂚', '𒂛', '𒂜', '𒂝', 
             '𒂞', '𒂟', '𒂠', '𒂡', '𒂢', '𒂣', '𒂤', '𒂥', '𒂦', '𒂧', '𒂨', '𒂩', '𒂪', '𒂫', '𒂬', '𒂭', '𒂮', '𒂯', '𒂰', '𒂱', '𒂲', '𒂳', '𒂴', 
             '𒂵', '𒂶', '𒂷', '𒂸', '𒂹', '𒂺', '𒂻', '𒂼', '𒂽', '𒂾', '𒂿', '𒃀', '𒃁', '𒃂', '𒃃', '𒃄', '𒃅', '𒃆', '𒃇', '𒃈', '𒃉', '𒃊', '𒃋', '𒃌', 
             '𒃍', '𒃎', '𒃏', '𒃐', '𒃑', '𒃒', '𒃓', '𒃔', '𒃕', '𒃖', '𒃗', '𒃘', '𒃙', '𒃚', '𒃛', '𒃜', '𒃝', '𒃞', '𒃟', '𒃠', '𒃡', '𒃢', '𒃣', '𒃤', 
             '𒃥', '𒃦', '𒃧', '𒃨', '𒃩', '𒃪', '𒃫', '𒃬', '𒃭', '𒃮', '𒃯', '𒃰', '𒃱', '𒃲', '𒃳', '𒃴', '𒃵', '𒃶', '𒃷', '𒃸', '𒃹', '𒃺', '𒃻', '𒃼', 
             '𒃽', '𒃾', '𒃿', '𒄀', '𒄁', '𒄂', '𒄃', '𒄄', '𒄅', '𒄆', '𒄇', '𒄈', '𒄉', '𒄊', '𒄋', '𒄌', '𒄍', '𒄎', '𒄏', '𒄐', '𒄑', '𒄒', 
             '𒄓', '𒄔', '𒄕', '𒄖', '𒄗', '𒄘', '𒄙', '𒄚', '𒄛', '𒄜', '𒄝', '𒄞', '𒄟', '𒄠', '𒄡', '𒄢', '𒄣', '𒄤', '𒄥', '𒄦', '𒄧', '𒄨', '𒄩', 
             '𒄪', '𒄫', '𒄬', '𒄭', '𒄮', '𒄯', '𒄰', '𒄱', '𒄲', '𒄳', '𒄴', '𒄵', '𒄶', '𒄷', '𒄸', '𒄹', '𒄺', '𒄻', '𒄼', '𒄽', '𒄾', '𒄿', '𒅀', '𒅁', '𒅂',
            '𒅃', '𒅄', '𒅅', '𒅆', '𒅇', '𒅈', '𒅉', '𒅊', '𒅋', '𒅌', '𒅍', '𒅎', '𒅏', '𒅐', '𒅑', '𒅒', '𒅓', '𒅔', '𒅕', '𒅖', '𒅗', 
            '𒅘', '𒅙', '𒅚', '𒅛', '𒅜', '𒅝', '𒅞', '𒅟', '𒅠', '𒅡', '𒅢', '𒅣', '𒅤', '𒅥', '𒅦', '𒅧', '𒅨', '𒅩', '𒅪', '𒅫', '𒅬', '𒅭', 
            '𒅮', '𒅯', '𒅰', '𒅱', '𒅲', '𒅳', '𒅴', '𒅵', '𒅶', '𒅷', '𒅸', '𒅹', '𒅺', '𒅻', '𒅼', '𒅽', '𒅾', '𒅿', '𒆀', '𒆁', '𒆂', '𒆃', 
            '𒆄', '𒆅', '𒆆', '𒆇', '𒆈', '𒆉', '𒆊', '𒆋', '𒆌', '𒆍', '𒆎', '𒆏', '𒆐', '𒆑', '𒆒', '𒆓', '𒆔', '𒆕', '𒆖', '𒆗', '𒆘', '𒆙', '𒆚', '𒆛', 
            '𒆜', '𒆝', '𒆞', '𒆟', '𒆠', '𒆡', '𒆢', '𒆣', '𒆤', '𒆥', '𒆦', '𒆧', '𒆨', '𒆩', '𒆪', '𒆫', '𒆬', '𒆭', '𒆮', '𒆯', '𒆰', '𒆱', '𒆲', '𒆳', 
            '𒆴', '𒆵', '𒆶', '𒆷', '𒆸', '𒆹', '𒆺', '𒆻', '𒆼', '𒆽', '𒆾', '𒆿', '𒇀', '𒇁', '𒇂', '𒇃', '𒇄', '𒇅', '𒇆', '𒇇', '𒇈', '𒇉', '𒇊', '𒇋', '𒇌', '𒇍', '𒇎',
              '𒇏', '𒇐', '𒇑', '𒇒', '𒇓', '𒇔', '𒇕', '𒇖', '𒇗', '𒇘', '𒇙', '𒇚', '𒇛', '𒇜', '𒇝', '𒇞', '𒇟', '𒇠', '𒇡', '𒇢', '𒇣', '𒇤', '𒇥', '𒇦', '𒇧', '𒇨', '𒇩',
                '𒇪', '𒇫', '𒇬', '𒇭', '𒇮', '𒇯', '𒇰', '𒇱', '𒇲', '𒇳', '𒇴', '𒇵', '𒇶', '𒇷', '𒇸', '𒇹', '𒇺', '𒇻', '𒇼', '𒇽', '𒇾', '𒇿', '𒈀', '𒈁', '𒈂',
                  '𒈃', '𒈄', '𒈅', '𒈆', '𒈇', '𒈈', '𒈉', '𒈊', '𒈋', '𒈌', '𒈍', '𒈎', '𒈏', '𒈐', '𒈑', '𒈒', '𒈓', '𒈔', '𒈕', '𒈖', '𒈗', '𒈘', 
                  '𒈙', '𒈚', '𒈛', '𒈜', '𒈝', '𒈞', '𒈟', '𒈠', '𒈡', '𒈢', '𒈣', '𒈤', '𒈥', '𒈦', '𒈧', '𒈨', '𒈩', '𒈪', '𒈫', '𒈬', '𒈭', '𒈮', '𒈯', 
                  '𒈰', '𒈱', '𒈲', '𒈳', '𒈴', '𒈵', '𒈶', '𒈷', '𒈸', '𒈹', '𒈺', '𒈻', '𒈼', '𒈽', '𒈾', '𒈿', '𒉀', '𒉁', '𒉂', '𒉃', '𒉄', '𒉅', '𒉆',
                    '𒉇', '𒉈', '𒉉', '𒉊', '𒉋', '𒉌', '𒉍', '𒉎', '𒉏', '𒉐', '𒉑', '𒉒', '𒉓', '𒉔', '𒉕', '𒉖', '𒉗', '𒉘', '𒉙', '𒉚', '𒉛', '𒉜', 
                    '𒉝', '𒉞', '𒉟', '𒉠', '𒉡', '𒉢', '𒉣', '𒉤', '𒉥', '𒉦', '𒉧', '𒉨', '𒉩', '𒉪', '𒉫', '𒉬', '𒉭', '𒉮', '𒉯', '𒉰', '𒉱', '𒉲',
                      '𒉳', '𒉴', '𒉵', '𒉶', '𒉷', '𒉸', '𒉹', '𒉺', '𒉻', '𒉼', '𒉽', '𒉾', '𒉿', '𒊀', '𒊁', '𒊂', '𒊃', '𒊄', '𒊅', '𒊆', '𒊇', '𒊈', 
                      '𒊉', '𒊊', '𒊋', '𒊌', '𒊍', '𒊎', '𒊏', '𒊐', '𒊑', '𒊒', '𒊓', '𒊔', '𒊕', '𒊖', '𒊗', '𒊘', '𒊙', '𒊚', '𒊛', '𒊜', '𒊝', '𒊞',
                        '𒊟', '𒊠', '𒊡', '𒊢', '𒊣', '𒊤', '𒊥', '𒊦', '𒊧', '𒊨', '𒊩', '𒊪', '𒊫', '𒊬', '𒊭', '𒊮', '𒊯', '𒊰', '𒊱', '𒊲', '𒊳', '𒊴', '𒊵', '𒊶',
                          '𒊷', '𒊸', '𒊹', '𒊺', '𒊻', '𒊼', '𒊽', '𒊾', '𒊿', '𒋀', '𒋁', '𒋂', '𒋃', '𒋄', '𒋅', '𒋆', '𒋇', '𒋈', '𒋉', '𒋊', '𒋋', 
                          '𒋌', '𒋍', '𒋎', '𒋏', '𒋐', '𒋑', '𒋒', '𒋓', '𒋔', '𒋕', '𒋖', '𒋗', '𒋘', '𒋙', '𒋚', '𒋛', '𒋜', '𒋝', '𒋞', '𒋟', '𒋠', '𒋡', 
                          '𒋢', '𒋣', '𒋤', '𒋥', '𒋦', '𒋧', '𒋨', '𒋩', '𒋪', '𒋫', '𒋬', '𒋭', '𒋮', '𒋯', '𒋰', '𒋱', '𒋲', '𒋳', '𒋴', '𒋵', '𒋶', '𒋷',
                            '𒋸', '𒋹', '𒋺', '𒋻', '𒋼', '𒋽', '𒋾', '𒋿', '𒌀', '𒌁', '𒌂', '𒌃', '𒌄', '𒌅', '𒌆', '𒌇', '𒌈', '𒌉', '𒌊', '𒌋', '𒌌', '𒌍', 
                            '𒌎', '𒌏', '𒌐', '𒌑', '𒌒', '𒌓', '𒌔', '𒌕', '𒌖', '𒌗', '𒌘', '𒌙', '𒌚', '𒌛', '𒌜', '𒌝', '𒌞', '𒌟', '𒌠', '𒌡', '𒌢', '𒌣', '𒌤', 
                            '𒌥', '𒌦', '𒌧', '𒌨', '𒌩', '𒌪', '𒌫', '𒌬', '𒌭', '𒌮', '𒌯', '𒌰', '𒌱', '𒌲', '𒌳', '𒌴', '𒌵', '𒌶', '𒌷', '𒌸', '𒌹',
                              '𒌺', '𒌻', '𒌼', '𒌽', '𒌾', '𒌿', '𒍀', '𒍁', '𒍂', '𒍃', '𒍄', '𒍅', '𒍆', '𒍇', '𒍈', '𒍉', '𒍊', '𒍋', '𒍌', '𒍍', '𒍎', '𒍏', 
                              '𒍐', '𒍑', '𒍒', '𒍓', '𒍔', '𒍕', '𒍖', '𒍗', '𒍘', '𒍙', '𒍚', '𒍛', '𒍜', '𒍝', '𒍞', '𒍟', '𒍠', '𒍡', '𒍢', '𒍣', '𒍤', '𒍥',
                                '𒍦', '𒍧', '𒍨', '𒍩', '𒍪', '𒍫', '𒍬', '𒍭', '𒍮', '𒍯', '𒍰', '𒍱', '𒍲', '𒍳', '𒍴', '𒍵', '𒍶', '𒍷', '𒍸', '𒍹', '𒍺',
                                  '𒍻', '𒍼', '𒍽', '𒍾', '𒍿', '𒎀', '𒎁', '𒎂', '𒎃', '𒎄', '𒎅', '𒎆', '𒎇', '𒎈', '𒎉', '𒎊', '𒎋', '𒎌', '𒎍', '𒎎',
                                    '𒎏', '𒎐', '𒎑', '𒎒', '𒎓', '𒎔', '𒎕', '𒎖', '𒎗', '𒎘', '𒎙', '𒐀', '𒐁', '𒐂', '𒐃', '𒐄', '𒐅', '𒐆', '𒐇', '𒐈', '𒐉',
                                      '𒐊', '𒐋', '𒐌', '𒐍', '𒐎', '𒐏', '𒐐', '𒐑', '𒐒', '𒐓', '𒐔', '𒐕', '𒐖', '𒐗', '𒐘', '𒐙', '𒐚', '𒐛', '𒐜', '𒐝', '𒐞', '𒐟', 
                                      '𒐠', '𒐡', '𒐢', '𒐣', '𒐤', '𒐥', '𒐦', '𒐧', '𒐨', '𒐩', '𒐪', '𒐫', '𒐬', '𒐭', '𒐮', '𒐯', 
                                      '𒐰', '𒐱', '𒐲', '𒐳', '𒐴', '𒐵', '𒐶', '𒐷', '𒐸', '𒐹', '𒐺', '𒐻', '𒐼', '𒐽', '𒐾', '𒐿', '𒑀', '𒑁', '𒑂', '𒑃', '𒑄', '𒑅',
                                        '𒑆', '𒑇', '𒑈', '𒑉', '𒑊', '𒑋', '𒑌', '𒑍', '𒑎', '𒑏', '𒑐', '𒑑', '𒑒', '𒑓', '𒑔', '𒑕', '𒑖', '𒑗', '𒑘', '𒑙', '𒑚', '𒑛', '𒑜', '𒑝',
                                          '𒑞', '𒑟', '𒑠', '𒑡', '𒑢', '𒑣', '𒑤', '𒑥', '𒑦', '𒑧', '𒑨', '𒑩', '𒑪', '𒑫', '𒑬', '𒑭', '𒑮', '𒑰', '𒑱', '𒑲', '𒑳', '𒑴']
hieroglpyhics = ['𓀀', '𓀁', '𓀂', '𓀃', '𓀄', '𓀅', '𓀆', '𓀇', '𓀈', '𓀉', '𓀊', '𓀋', '𓀌', '𓀍', '𓀎', '𓀏', '𓀐', '𓀑', '𓀒', '𓀓', '𓀔', '𓀕', '𓀖', '𓀗', '𓀘', '𓀙', '𓀚', '𓀛', '𓀜', '𓀝', '𓀞', 
    '𓀟', '𓀠', '𓀡', '𓀢', '𓀣', '𓀤', '𓀥', '𓀦', '𓀧', '𓀨', '𓀩', '𓀪', '𓀫', '𓀬', '𓀭', '𓀮', '𓀯', '𓀰', '𓀱', '𓀲', '𓀳', '𓀴', '𓀵', '𓀶', '𓀷', '𓀸', '𓀹', '𓀺', '𓀻', '𓀼', '𓀽', '𓀾', '𓀿', '𓁀',
    '𓁁', '𓁂', '𓁃', '𓁄', '𓁅', '𓁆', '𓁇', '𓁈', '𓁉', '𓁊', '𓁋', '𓁌', '𓁍', '𓁎', '𓁏', '𓁐', '𓁑', '𓁒', '𓁓', '𓁔', '𓁕', '𓁖', '𓁗', '𓁘', '𓁙', '𓁚', '𓁛', '𓁜', '𓁝', '𓁞', '𓁟', '𓁠', '𓁡', '𓁢', 
    '𓁣', '𓁤', '𓁥', '𓁦', '𓁧', '𓁨', '𓁩', '𓁪', '𓁫', '𓁬', '𓁭', '𓁮', '𓁯', '𓁰', '𓁱', '𓁲', '𓁳', '𓁴', '𓁵', '𓁶', '𓁷', '𓁸', '𓁹', '𓁺', '𓁻', '𓁼', '𓁽', '𓁾', '𓁿', '𓂀', '𓂁', '𓂂', '𓂃', 
    '𓂄', '𓂅', '𓂆', '𓂇', '𓂈', '𓂉', '𓂊', '𓂋', '𓂌', '𓂍', '𓂎', '𓂏', '𓂐', '𓂑', '𓂒', '𓂓', '𓂔', '𓂕', '𓂖', '𓂗', '𓂘', '𓂙', '𓂚', '𓂛', '𓂜', '𓂝', '𓂞', '𓂟', '𓂠', '𓂡', '𓂢', '𓂣', 
    '𓂤', '𓂥', '𓂦', '𓂧', '𓂨', '𓂩', '𓂪', '𓂫', '𓂬', '𓂭', '𓂮', '𓂯', '𓂰', '𓂱', '𓂲', '𓂳', '𓂴', '𓂵', '𓂶', '𓂷', '𓂸', '𓂹', '𓂺', '𓂻', '𓂼', '𓂽', '𓂾', '𓂿', '𓃀', '𓃁', '𓃂', '𓃃', 
    '𓃄', '𓃅', '𓃆', '𓃇', '𓃈', '𓃉', '𓃊', '𓃋', '𓃌', '𓃍', '𓃎', '𓃏', '𓃐', '𓃑', '𓃒', '𓃓', '𓃔', '𓃕', '𓃖', '𓃗', '𓃘', '𓃙', '𓃚', '𓃛', '𓃜', '𓃝', '𓃞', '𓃟', '𓃠', '𓃡', '𓃢', 
    '𓃣', '𓃤', '𓃥', '𓃦', '𓃧', '𓃨', '𓃩', '𓃪', '𓃫', '𓃬', '𓃭', '𓃮', '𓃯', '𓃰', '𓃱', '𓃲', '𓃳', '𓃴', '𓃵', '𓃶', '𓃷', '𓃸', '𓃹', '𓃺', '𓃻', '𓃼', '𓃽', '𓃾', '𓃿', '𓄀', '𓄁', 
    '𓄂', '𓄃', '𓄄', '𓄅', '𓄆', '𓄇', '𓄈', '𓄉', '𓄊', '𓄋', '𓄌', '𓄍', '𓄎', '𓄏', '𓄐', '𓄑', '𓄒', '𓄓', '𓄔', '𓄕', '𓄖', '𓄗', '𓄘', '𓄙', '𓄚', '𓄛', '𓄜', '𓄝', '𓄞', '𓄟', '𓄠', '𓄡', 
    '𓄢', '𓄣', '𓄤', '𓄥', '𓄦', '𓄧', '𓄨', '𓄩', '𓄪', '𓄫', '𓄬', '𓄭', '𓄮', '𓄯', '𓄰', '𓄱', '𓄲', '𓄳', '𓄴', '𓄵', '𓄶', '𓄷', '𓄸', '𓄹', '𓄺', '𓄻', '𓄼', '𓄽', '𓄾', '𓄿', '𓅀', 
    '𓅁', '𓅂', '𓅃', '𓅄', '𓅅', '𓅆', '𓅇', '𓅈', '𓅉', '𓅊', '𓅋', '𓅌', '𓅍', '𓅎', '𓅏', '𓅐', '𓅑', '𓅒', '𓅓', '𓅔', '𓅕', '𓅖', '𓅗', '𓅘', '𓅙', '𓅚', '𓅛', '𓅜', '𓅝', '𓅞', 
    '𓅟', '𓅠', '𓅡', '𓅢', '𓅣', '𓅤', '𓅥', '𓅦', '𓅧', '𓅨', '𓅩', '𓅪', '𓅫', '𓅬', '𓅭', '𓅮', '𓅯', '𓅰', '𓅱', '𓅲', '𓅳', '𓅴', '𓅵', '𓅶', '𓅷', '𓅸', '𓅹', '𓅺', '𓅻', '𓅼', 
    '𓅽', '𓅾', '𓅿', '𓆀', '𓆁', '𓆂', '𓆃', '𓆄', '𓆅', '𓆆', '𓆇', '𓆈', '𓆉', '𓆊', '𓆋', '𓆌', '𓆍', '𓆎', '𓆏', '𓆐', '𓆑', '𓆒', '𓆓', '𓆔', '𓆕', '𓆖', '𓆗', '𓆘', '𓆙', '𓆚', '𓆛', 
    '𓆜', '𓆝', '𓆞', '𓆟', '𓆠', '𓆡', '𓆢', '𓆣', '𓆤', '𓆥', '𓆦', '𓆧', '𓆨', '𓆩', '𓆪', '𓆫', '𓆬', '𓆭', '𓆮', '𓆯', '𓆰', '𓆱', '𓆲', '𓆳', '𓆴', '𓆵', '𓆶', '𓆷', '𓆸', '𓆹', '𓆺', '𓆻', 
    '𓆼', '𓆽', '𓆾', '𓆿', '𓇀', '𓇁', '𓇂', '𓇃', '𓇄', '𓇅', '𓇆', '𓇇', '𓇈', '𓇉', '𓇊', '𓇋', '𓇌', '𓇍', '𓇎', '𓇏', '𓇐', '𓇑', '𓇒', '𓇓', '𓇔', '𓇕', '𓇖', '𓇗', '𓇘', '𓇙', '𓇚', '𓇛', '𓇜', '𓇝', 
    '𓇞', '𓇟', '𓇠', '𓇡', '𓇢', '𓇣', '𓇤', '𓇥', '𓇦', '𓇧', '𓇨', '𓇩', '𓇪', '𓇫', '𓇬', '𓇭', '𓇮', '𓇯', '𓇰', '𓇱', '𓇲', '𓇳', '𓇴', '𓇵', '𓇶', '𓇷', '𓇸', '𓇹', '𓇺', '𓇻', '𓇼', '𓇽', '𓇾', '𓇿', 
    '𓈀', '𓈁', '𓈂', '𓈃', '𓈄', '𓈅', '𓈆', '𓈇', '𓈈', '𓈉', '𓈊', '𓈋', '𓈌', '𓈍', '𓈎', '𓈏', '𓈐', '𓈑', '𓈒', '𓈓', '𓈔', '𓈕', '𓈖', '𓈗', '𓈘', '𓈙', '𓈚', '𓈛', '𓈜', '𓈝', '𓈞', '𓈟', 
    '𓈠', '𓈡', '𓈢', '𓈣', '𓈤', '𓈥', '𓈦', '𓈧', '𓈨', '𓈩', '𓈪', '𓈫', '𓈬', '𓈭', '𓈮', '𓈯', '𓈰', '𓈱', '𓈲', '𓈳', '𓈴', '𓈵', '𓈶', '𓈷', '𓈸', '𓈹', '𓈺', '𓈻', '𓈼', '𓈽', '𓈾', '𓈿', 
    '𓉀', '𓉁', '𓉂', '𓉃', '𓉄', '𓉅', '𓉆', '𓉇', '𓉈', '𓉉', '𓉊', '𓉋', '𓉌', '𓉍', '𓉎', '𓉏', '𓉐', '𓉑', '𓉒', '𓉓', '𓉔', '𓉕', '𓉖', '𓉗', '𓉘', '𓉙', '𓉚', '𓉛', '𓉜', '𓉝', '𓉞', '𓉟', '𓉠', 
    '𓉡', '𓉢', '𓉣', '𓉤', '𓉥', '𓉦', '𓉧', '𓉨', '𓉩', '𓉪', '𓉫', '𓉬', '𓉭', '𓉮', '𓉯', '𓉰', '𓉱', '𓉲', '𓉳', '𓉴', '𓉵', '𓉶', '𓉷', '𓉸', '𓉹', '𓉺', '𓉻',  '𓉼', '𓉽', '𓉾', '𓉿', '𓊀', 
    '𓊁', '𓊂', '𓊃', '𓊄', '𓊅', '𓊆', '𓊇', '𓊈', '𓊉', '𓊊', '𓊋', '𓊌', '𓊍', '𓊎', '𓊏', '𓊐', '𓊑', '𓊒', '𓊓', '𓊔', '𓊕', '𓊖', '𓊗', '𓊘', '𓊙', '𓊚', '𓊛', '𓊜', '𓊝', '𓊞', '𓊟', '𓊠', '𓊡', 
    '𓊢', '𓊣', '𓊤', '𓊥', '𓊦', '𓊧', '𓊨', '𓊩', '𓊪', '𓊫', '𓊬', '𓊭', '𓊮', '𓊯', '𓊰', '𓊱', '𓊲', '𓊳', '𓊴', '𓊵', '𓊶', '𓊷', '𓊸', '𓊹', '𓊺', '𓊻', '𓊼', '𓊽', '𓊾', '𓊿', '𓋀', '𓋁', '𓋂', 
    '𓋃', '𓋄', '𓋅', '𓋆', '𓋇', '𓋈', '𓋉', '𓋊', '𓋋', '𓋌', '𓋍', '𓋎', '𓋏', '𓋐', '𓋑', '𓋒', '𓋓', '𓋔', '𓋕', '𓋖', '𓋗', '𓋘', '𓋙', '𓋚', '𓋛', '𓋜', '𓋝', '𓋞', '𓋟', '𓋠', '𓋡', '𓋢', '𓋣', 
    '𓋤', '𓋥', '𓋦', '𓋧', '𓋨', '𓋩', '𓋪', '𓋫', '𓋬', '𓋭', '𓋮', '𓋯', '𓋰', '𓋱', '𓋲', '𓋳', '𓋴', '𓋵', '𓋶', '𓋷', '𓋸', '𓋹', '𓋺', '𓋻', '𓋼', '𓋽', '𓋾', '𓋿', '𓌀', '𓌁', '𓌂', '𓌃', '𓌄', 
    '𓌅', '𓌆', '𓌇', '𓌈', '𓌉', '𓌊', '𓌋', '𓌌', '𓌍', '𓌎', '𓌏', '𓌐', '𓌑', '𓌒', '𓌓', '𓌔', '𓌕', '𓌖', '𓌗', '𓌘', '𓌙', '𓌚', '𓌛', '𓌜', '𓌝', '𓌞', '𓌟', '𓌠', '𓌡', '𓌢', '𓌣', '𓌤', '𓌥', '𓌦', 
    '𓌧', '𓌨', '𓌩', '𓌪', '𓌫', '𓌬', '𓌭', '𓌮', '𓌯', '𓌰', '𓌱', '𓌲', '𓌳', '𓌴', '𓌵', '𓌶', '𓌷', '𓌸', '𓌹', '𓌺', '𓌻', '𓌼', '𓌽', '𓌾', '𓌿', '𓍀', '𓍁', '𓍂', '𓍃', '𓍄', '𓍅', '𓍆', 
    '𓍇', '𓍈', '𓍉', '𓍊', '𓍋', '𓍌', '𓍍', '𓍎', '𓍏', '𓍐', '𓍑', '𓍒', '𓍓', '𓍔', '𓍕', '𓍖', '𓍗', '𓍘', '𓍙', '𓍚', '𓍛', '𓍜', '𓍝', '𓍞', '𓍟', '𓍠', '𓍡', '𓍢', '𓍣', '𓍤', '𓍥', '𓍦', '𓍧', '𓍨', '𓍩', 
    '𓍪', '𓍫', '𓍬', '𓍭', '𓍮', '𓍯', '𓍰', '𓍱', '𓍲', '𓍳', '𓍴', '𓍵', '𓍶', '𓍷', '𓍸', '𓍹', '𓍺', '𓍻', '𓍼', '𓍽', '𓍾', '𓍿', '𓎀', '𓎁', '𓎂', '𓎃', '𓎄', '𓎅', '𓎆', '𓎇', '𓎈', '𓎉', '𓎊', 
    '𓎋', '𓎌', '𓎍', '𓎎', '𓎏', '𓎐', '𓎑', '𓎒', '𓎓', '𓎔', '𓎕', '𓎖', '𓎗', '𓎘', '𓎙', '𓎚', '𓎛', '𓎜', '𓎝', '𓎞', '𓎟', '𓎠', '𓎡', '𓎢', '𓎣', '𓎤', '𓎥', '𓎦', '𓎧', '𓎨', '𓎩', '𓎪', 
    '𓎫', '𓎬', '𓎭', '𓎮', '𓎯', '𓎰', '𓎱', '𓎲', '𓎳', '𓎴', '𓎵', '𓎶', '𓎷', '𓎸', '𓎹', '𓎺', '𓎻', '𓎼', '𓎽', '𓎾', '𓎿', '𓏀', '𓏁', '𓏂', '𓏃', '𓏄', '𓏅', '𓏆', '𓏇', '𓏈', '𓏉', '𓏊', '𓏋', '𓏌', 
    '𓏍', '𓏎', '𓏏', '𓏐', '𓏑', '𓏒', '𓏓', '𓏔', '𓏕', '𓏖', '𓏗', '𓏘', '𓏙', '𓏚', '𓏛', '𓏜', '𓏝', '𓏞', '𓏟', '𓏠', '𓏡', '𓏢', '𓏣', '𓏤', '𓏥', '𓏦', '𓏧', '𓏨', '𓏩', '𓏪', '𓏫', '𓏬', '𓏭', '𓏮', 
    '𓏯', '𓏰', '𓏱', '𓏲', '𓏳', '𓏴', '𓏵', '𓏶', '𓏷', '𓏸', '𓏹', '𓏺', '𓏻', '𓏼', '𓏽', '𓏾', '𓏿', '𓐀', '𓐁', '𓐂', '𓐃', '𓐄', '𓐅', '𓐆', '𓐇', '𓐈', '𓐉', '𓐊', '𓐋', '𓐌', '𓐍', '𓐎', '𓐏', '𓐐', '𓐑', 
    '𓐒', '𓐓', '𓐔', '𓐕', '𓐖', '𓐗', '𓐘', '𓐙', '𓐚', '𓐛', '𓐜', '𓐝', '𓐞', '𓐟', '𓐠', '𓐡', '𓐢', '𓐣', '𓐤', '𓐥', '𓐦', '𓐧', '𓐨', '𓐩', '𓐪', '𓐫', '𓐬', '𓐭', '𓐮']

sillyfont = cuneiform
sillyfontName = "cuneiform"
x = []
randomizer = random.Random()
seed = datetime.now().microsecond * datetime.now().second
print("This is the seed: ", seed)
randomizer.seed(seed)
option = 0
while(option != -1):
    print("Choose how many " + sillyfontName + " letters to generate (-1 to end): ", end="")
    option = int(input())
    if(option != -1):
        sentence  = ""
        print("Choose how many spaces to include randomly: ", end="")
        spaces = int(input())
        for i in range(0, option):
            if(spaces != 0 and (i != 0 or i != option)):
                if(random.randrange(0, 10) > 7):
                    sentence += " "
                    spaces -= 1
            sentence += sillyfont[random.randrange(0, sillyfont.__len__())]
        print(sentence)
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file = open(os.path.join(__location__, 'outputs/format.txt'), "w", encoding="utf-8")
        file.write(sentence)
        file.close()