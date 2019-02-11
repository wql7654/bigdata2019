
def show_candidates(candidate_list):
    for idol_list in candidate_list:
        print("%s\n"%idol_list[:2],end='')


def make_idol(candidate_list):
    for idol_list in candidate_list:
        print("신예 아이돌 %s 인기 급상승\n" % idol_list[:2], end='')

def make_world_star(candidate_list):
    for idol_list in candidate_list:
        print("아이돌 %s 월드스타 등극\n" % idol_list[:2], end='')





f = open("./연습생.txt",'r', encoding="UTF-8")
candidate_list=f.readlines()
print(candidate_list)

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)
f.close()