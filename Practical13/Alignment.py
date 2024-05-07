human="METTPLNSQKQLSACEDGEDCQENGVLQKVVPTPGDKVESGQISNGYSAVPSPGAGDDT RHSIPATTTTLVAELHQGERETWGKKVDFLLSVIGYAVDLGNVWRFPYICYQNGGGAFL LPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIMA WALYYLISSFTDQLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQI HRSKGLQDLGGISWQLALCIMLIFTVIYFSIWKGVKTSGKVVWVTATFPYIILSVLLVRGA TLPGAWRGVLFYLKPNWQKLLETGVWIDAAAQIFFSLGPGFGVLLAFASYNKFNNNCY QDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANM PASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHVWAKRRERFVLAVVITCFFGSL VTLTFGGAYVVKLLEEYATGPAVLTVALIEAVAVSWFYGITQFCRDVKEMLGFSPGWF WRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPYWSIILGYCIGTSSFICIPTYIAYRLIITP GTFKERIIKSITPETPTEIPCGDIRLNAV"
mouse="METTPLNSQKVLSECKDKEDCQENGVLQKGVPTPADKAGPGQISNGYSAVPSTSAGDEA PHSTPAATTTLVAEIHQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFL LPYTIMAIFGGIPLFYMELALGQYHRNGCISIWKKICPIFKGIGYAICIIAFYIASYYNTIIAW ALYYLISSFTDQLPWTSCKNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQ SKGLQDLGTISWQLALCIMLIFTIIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATL PGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQ DALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMP ASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCILGSLLT LTSGGAYVVTLLEEYATGPAVLTVALIEAVVVSWFYGITQFCSDVKEMLGFSPGWFWRI CWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIILGYCIGTSSVICIPIYIIYRLISTPGTL KERIIKSITPETPTEIPCGDIRMNAV"
rat="METTPLNSQKVLSECKDREDCQENGVLQKGVPTTADRAEPSQISNGYSAVPSTSAGDEA SHSIPAATTTLVAEIRQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLL PYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIIAWA LYYLISSLTDRLPWTSCTNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQS KGLQDLGTISWQLTLCIVLIFTVIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLP GAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQD ALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPA STFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCVLGSLLTL TSGGAYVVTLLEEYATGPAVLTVALIEAVAVSWFYGITQFCSDVKEMLGFSPGWFWRIC WVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIVLGYCIGMSSVICIPTYIIYRLISTPGTL KERIIKSITPETPTEIPCGDIRMNAV"
human=human.replace(" ","")
mouse=mouse.replace(" ","")
rat=rat.replace(" ","")
a=len(human)

amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
blosum = [[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],]



def calculation(seq1, seq2) :
    same=0
    alignment_score=0
    percentage=0
    
    for i in range(a) :
        aa1=amino.index(seq1[i])
        aa2=amino.index(seq2[i])
        alignment_score+=blosum[aa1][aa2]
        if seq1[i]==seq2[i] :
            same+=1
        percentage=same/a
    
    return percentage, alignment_score

human_mouse=calculation(human, mouse)
alignment_score_human_mouse=human_mouse[1]
percentage_human_mouse=human_mouse[0]
human_rat=calculation(human, rat)
alignment_score_human_rat=human_rat[1]
percentage_human_rat=human_rat[0] 
rat_mouse=calculation(rat, mouse)
alignment_score_rat_mouse=rat_mouse[1]
percentage_rat_mouse=rat_mouse[0]

print("seq1: human seq2: mouse \n ", "alignment score= ", alignment_score_human_mouse, "identity= ", percentage_human_mouse*100, "% \n" )
print("seq1: human seq2: rat \n ", "alignment score= ", alignment_score_human_rat, "identity= ", percentage_human_rat*100, "% \n" )
print("seq1: rat seq2: mouse \n ", "alignment score= ", alignment_score_rat_mouse, "identity= ", percentage_rat_mouse*100, "%" )
