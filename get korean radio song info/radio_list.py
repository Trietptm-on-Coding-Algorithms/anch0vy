#broad,title,broad_time,radio_url,_filter,must_have_word,block_word
import urllib
from xml.etree.ElementTree import parse
rlist=[
["kbs_cool_fm",	u"장윤주의 옥탑방 라디오",			"",		"826",		"1491",		"",		""],
["kbs_cool_fm",	u"나얼의 음악세계",				"",		"826",		"1371",		"",		""],#prob
["kbs_cool_fm",	u"더 가까이 정지원입니다",			"",		"826",		"1597",		"",		""],
["kbs_cool_fm",	u"정다은의 상쾌한 아침",			"",		"826",		"861",		"",		""],
["kbs_cool_fm",	u"이근철의 굿모닝팝스",			"",		"826",		"232",		"",		""],
["kbs_cool_fm",	u"황정민의 FM대행진",			"",		"826",		"233",		"",		""],
["kbs_cool_fm",	u"이현우의 음악앨범",				"",		"826",		"77",		"",		""],
["kbs_cool_fm",	u"최다니엘의 팝스팝스",			"",		"826",		"1594",		"",		""],
["kbs_cool_fm",	u"이소라의 가요광장",				"",		"826",		"1595",		"",		""],
["kbs_cool_fm",	u"조정치 장동민의 2시",			"",		"826",		"1596",		"",		""],
["kbs_cool_fm",	u"김C의 뮤직쇼",				"",		"826",		"1537",		"",		""],
["kbs_cool_fm",	u"사랑하기 좋은날 이금희입니다",		"",		"826",		"199",		"",		""],
["kbs_cool_fm",	u"유인나의 볼륨을 높여요",			"",		"826",		"1369",		"",		""],
["kbs_cool_fm",	u"슈퍼주니어의 키스 더 라디오",		"",		"826",		"209",		"",		""],
["sbs_power_fm",u"장예원의 오늘 같은 밤",			"",		"night_yewon",										"",		"",			""],
["sbs_power_fm",u"이동진의 그럼에도 불구하고",		"",		"djdj",												"",		"",			""],
["sbs_power_fm",u"애프터 클럽",					"",		"afterclub",										"",		"",			""],
["sbs_power_fm",u"조정식의 사운드오브뮤직",			"",		"som2",												"",		"",			""],
["sbs_power_fm",u"김영철의 펀펀투데이",			"",		"funfun",											"",		"",			""],
["sbs_power_fm",u"호란의 파워FM",				"",		"power_fm",											"",		"",			""],
["sbs_power_fm",u"아름다운 이 아침 김창완 입니다",	"",		"morningchang",										"",		"",			""],
["sbs_power_fm",u"공형진의 씨네타운",				"",		"cine",												"",		"",			""],
["sbs_power_fm",u"최화정의 파워타임",				"",		"powertime",										"",		"",			""],
["sbs_power_fm",u"두시탈출 컬투쇼",				"",		"cultwoshow",										"",		"",			""],
["sbs_power_fm",u"올드스쿨",					"",		"oldschool",										"",		"",			""],
["sbs_power_fm",u"박소현의 러브게임",				"",		"lovegame",											"",		"",			""],
["sbs_power_fm",u"케이윌의 영스트리트",			"",		"youngstreet",										"",		"",			""],
["sbs_power_fm",u"장기하의 대단한 라디오",			"",		"greatradio",										"",		"",			""],
["sbs_love_fm",u"김태욱의 기분좋은 밤",			"",		"goodnight",										"",		"",			""],
["sbs_love_fm",u"이현경의 뮤직토피아",			"",		"musictopia",										"",		"",			""],
["sbs_love_fm",u"이숙영의 러브FM",				"",		"love_fm",											"",		"",			""],
["sbs_love_fm",u"김지선,김일중의 세상을 만나자",		"",		"world09",											"",		"",			""],
["sbs_love_fm",u"노사연, 이성미쇼",				"",		"noleeshow",										"",		"",			""],
["sbs_love_fm",u"유영재의 가요쇼",				"",		"yushow",											"",		"",			""],
["sbs_love_fm",u"박영진, 박지선의 명랑특급",		"",		"myungrang",										"",		"",			""],
["sbs_love_fm",u"박은경의 스위트 뮤직 박스",		"",		"musicbox",											"",		"",			""],
["sbs_love_fm",u"최백호의 낭만시대",				"",		"romanticage",										"",		"",			""],
]

#mbc
#broad_name,title,time,broadcastid,groupid
tree=parse(urllib.urlopen('http://miniunit.imbc.com/Schedule'))
_zip=zip(tree.getiterator('Channel'),tree.getiterator("ProgramTitle"),tree.getiterator('StartTime'),
	tree.getiterator('RunningTime'),tree.getiterator('BroadCastID'),tree.getiterator('ProgramGroupID'))
for channel,title,start,running,bid,gid in _zip:
	channel=channel.text
	title=title.text
	bid=bid.text
	gid=gid.text
	start_h=int(start.text[:2])
	start_m=int(start.text[2:])
	running_h=int(running.text)/60
	running_m=int(running.text)%60
	_time='%02d:%02d-%02d:%02d'%(start_h,start_m,(start_h+running_h+(running_h+running_m)/60)%24,(running_h+running_m)%60)
	rlist.append(['mbc'+channel,title,_time,gid,bid,'dummy','dummy'])

if __name__ == '__main__':
	for x in rlist:
		print x