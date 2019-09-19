# Fyrsta og síðasta staf sérhvers orðs á ekki að brengla. 
# Ef greinarmerki er í enda orðs (t.d. problem.), þá skal ekki eiga við greinarmerkið 
# og það telur jafnframt ekki sem síðasti óbrenglaði stafurinn (í rununni problem. er m þá síðasti 
# stafurinn sem ekki á að brengla). Þegar athugað er hvort safur sé greinarmerki þá ber að nota 
# string.punctuation (sjá bls. 253 í kennslubókinni).
# Annars á að brengla stafina á milli fyrsta og síðasta stafs sérhvers orðs með því að skipta (víxla) 
# á aðliggjandi stöfum (byrja vinstra megin).