# -*- coding: utf-8 -*-
from dbtool import dbtool,radiodb_init
from bs4 import BeautifulSoup
from werkzeug.exceptions import HTTPException
import urllib2,os,sys,datetime,time
import simplejson as json
from youtube import youtube_search
DEBUG=1
#2014.12.27
tag2=u'''[
  {
    "items": [
      {
        "programId": "749",
        "imageSrc": "http://cfile188.uf.daum.net/image/256A9147532AB2E913CD11",
        "programMasterName": "12시에 만납시다 김필원입니다",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "1200",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "1481",
        "imageSrc": "http://cfile140.uf.daum.net/image/261E183353323A5027AE81",
        "programMasterName": "정오의 희망곡 김신영입니다",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "1200",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "347",
        "imageSrc": "http://cfile188.uf.daum.net/image/246DB23853323A6E0E6752",
        "programMasterName": "최화정의 파워타임",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "1200",
        "channelEngName": "sbspw"
      },
      {
        "programId": "1595",
        "imageSrc": "http://cfile188.uf.daum.net/image/2558A047532AB39B20AB1A",
        "programMasterName": "이소라의 가요광장",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "1200",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1563",
        "imageSrc": "http://cfile90.uf.daum.net/image/2221213A5332544D011D8C",
        "programMasterName": "이세준, 최재훈의 도시락쇼",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "1210",
        "channelEngName": "sbslove"
      },
      {
        "programId": "114",
        "imageSrc": "http://cfile80.uf.daum.net/image/2421614A533B923010378D",
        "programMasterName": "강원래의 노래선물",
        "description": "",
        "channelName": "KBS 사랑의소리",
        "channelId": "828",
        "channelType": "4",
        "broadcastTime": "1210",
        "channelEngName": "kbslove"
      },
      {
        "programId": "295",
        "imageSrc": "http://cfile140.uf.daum.net/image/253DAB4A532AB3152B1E10",
        "programMasterName": "박승화의 가요속으로",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "1600",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "1482",
        "imageSrc": "http://cfile20.uf.daum.net/image/24470C39533253830F3AE6",
        "programMasterName": "오후의 발견, 김현철입니다",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "1600",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "368",
        "imageSrc": "http://cfile190.uf.daum.net/image/21090838533254A122CB54",
        "programMasterName": "김창렬의 올드스쿨",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "1600",
        "channelEngName": "sbspw"
      },
      {
        "programId": "852",
        "imageSrc": "http://cfile138.uf.daum.net/image/2175D236533254B2085767",
        "programMasterName": "박소현의 러브게임",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "1800",
        "channelEngName": "sbspw"
      },
      {
        "programId": "199",
        "imageSrc": "http://cfile136.uf.daum.net/image/233C7B49533240F316F7F7",
        "programMasterName": "사랑하기 좋은 날 이금희입니다",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "1800",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1438",
        "imageSrc": "http://cfile140.uf.daum.net/image/23192548533B66712F9434",
        "programMasterName": "박영진, 박지선의 명랑특급",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "1805",
        "channelEngName": "sbslove"
      }
    ]
  },
  {
    "items": [
      {
        "programId": "1586",
        "imageSrc": "http://cfile4.uf.daum.net/image/2223BC3F53716D6F06EE3F",
        "programMasterName": "써니의 FM데이트",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "2000",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "297",
        "imageSrc": "http://cfile137.uf.daum.net/image/221A1C49532AB3492802FA",
        "programMasterName": "오미희의 행복한 동행",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "2000",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "1369",
        "imageSrc": "http://cfile181.uf.daum.net/image/2139AA4F5332410E30DE3F",
        "programMasterName": "유인나의 볼륨을 높여요",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "2000",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "209",
        "imageSrc": "http://cfile176.uf.daum.net/image/2703FE4A533240FE1D67EC",
        "programMasterName": "슈퍼주니어의 키스 더 라디오",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "2200",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "298",
        "imageSrc": "http://cfile188.uf.daum.net/image/257DDB4B53323F3112560E",
        "programMasterName": "허윤희의 꿈과 음악사이에",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "2200",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "24",
        "imageSrc": "http://cfile184.uf.daum.net/image/2217AE3C546BF4332F54A3",
        "programMasterName": "허경환의 별이 빛나는 밤에",
        "description": "",
        "channelName": "MBC표준FM",
        "channelId": "832",
        "channelType": "4",
        "broadcastTime": "2205",
        "channelEngName": "mbcfm"
      }
    ]
  }
]
'''

tag9=u'''[
  {
    "items": [
      {
        "programId": "399",
        "imageSrc": "http://cfile189.uf.daum.net/image/276A0B4253313EFC037137",
        "programMasterName": "푸른밤 종현입니다",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "0000",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "1496",
        "imageSrc": "http://cfile109.uf.daum.net/image/232631465350C55E1900D2",
        "programMasterName": "달콤한 밤, 허수경입니다",
        "description": "",
        "channelName": "TBS 교통방송",
        "channelId": "837",
        "channelType": "4",
        "broadcastTime": "0000",
        "channelEngName": "tbs"
      },
      {
        "programId": "851",
        "imageSrc": "http://cfile189.uf.daum.net/image/22538D3A53325424280AEC",
        "programMasterName": "김태욱의 기분좋은 밤",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "0000",
        "channelEngName": "sbslove"
      },
      {
        "programId": "25",
        "imageSrc": "http://cfile189.uf.daum.net/image/2277C53B53BB48B02FF274",
        "programMasterName": "정준영의 심심타파",
        "description": "",
        "channelName": "MBC표준FM",
        "channelId": "832",
        "channelType": "4",
        "broadcastTime": "0005",
        "channelEngName": "mbcfm"
      },
      {
        "programId": "1641",
        "imageSrc": "http://cfile36.uf.daum.net/image/235D0942537AB0CA2202EF",
        "programMasterName": "레인보우 스트리트",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "0200",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "1141",
        "imageSrc": "http://cfile9.uf.daum.net/image/27698C4553CC75FB1C189D",
        "programMasterName": "이현경의 뮤직토피아",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "0200",
        "channelEngName": "sbslove"
      },
      {
        "programId": "1626",
        "imageSrc": "http://cfile9.uf.daum.net/image/2379CD4B5350C21112CE9B",
        "programMasterName": "이동진의 그럼에도 불구하고",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "0200",
        "channelEngName": "sbspw"
      },
      {
        "programId": "1597",
        "imageSrc": "http://cfile5.uf.daum.net/image/226F7F4C532AB44D1A9997",
        "programMasterName": "더 가까이 정지원입니다",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "0300",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1565",
        "imageSrc": "http://cfile185.uf.daum.net/image/213FCB3B53352028309D36",
        "programMasterName": "애프터 클럽",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "0300",
        "channelEngName": "sbspw"
      },
      {
        "programId": "330",
        "imageSrc": "http://cfile40.uf.daum.net/image/2619F84A533B65A12C03C9",
        "programMasterName": "조정식의 사운드오브뮤직",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "0400",
        "channelEngName": "sbspw"
      },
      {
        "programId": "861",
        "imageSrc": "http://cfile137.uf.daum.net/image/236D9A3B534C9844087BBC",
        "programMasterName": "정다은의 상쾌한 아침",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "0500",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1487",
        "imageSrc": "http://cfile84.uf.daum.net/image/255CDD34546BF2D516BB11",
        "programMasterName": "세상을 여는 아침 이재은입니다",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "0600",
        "channelEngName": "mbcfm4u"
      }
    ]
  },
  {
    "items": [
      {
        "programId": "233",
        "imageSrc": "http://cfile189.uf.daum.net/image/261C2848532AB3E82580D5",
        "programMasterName": "황정민의 FM대행진",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "0700",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1642",
        "imageSrc": "http://cfile36.uf.daum.net/image/234CD549537AA6DC30D440",
        "programMasterName": "호란의 파워FM",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "0700",
        "channelEngName": "sbspw"
      },
      {
        "programId": "1588",
        "imageSrc": "http://cfile2.uf.daum.net/image/274B4A335332545531B052",
        "programMasterName": "이숙영의 러브FM",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "0830",
        "channelEngName": "sbslove"
      },
      {
        "programId": "345",
        "imageSrc": "http://cfile103.uf.daum.net/image/26383534533254A9213CC2",
        "programMasterName": "아름다운 이 아침 김창완입니다",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "0900",
        "channelEngName": "sbspw"
      },
      {
        "programId": "77",
        "imageSrc": "http://cfile181.uf.daum.net/image/2374BC50532AB3D018BB5A",
        "programMasterName": "이현우의 음악앨범",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "0900",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1480",
        "imageSrc": "http://cfile40.uf.daum.net/image/242E7235533253790C7E78",
        "programMasterName": "오늘 아침 정지영입니다",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "0900",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "903",
        "imageSrc": "http://cfile101.uf.daum.net/image/26407F3B533520EC2CB3A7",
        "programMasterName": "김지선, 김일중의 세상을 만나자",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "1005",
        "channelEngName": "sbslove"
      },
      {
        "programId": "348",
        "imageSrc": "http://cfile8.uf.daum.net/image/226F7A3C533254D823E8F5",
        "programMasterName": "두시탈출 컬투쇼",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "1400",
        "channelEngName": "sbspw"
      },
      {
        "programId": "252",
        "imageSrc": "http://cfile182.uf.daum.net/image/231394375332534D093E90",
        "programMasterName": "두시의데이트 박경림입니다",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "1400",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "1643",
        "imageSrc": "http://cfile20.uf.daum.net/image/260DD14F54167A3D0A6EDC",
        "programMasterName": "라디오 3.0 이병진입니다",
        "description": "",
        "channelName": "CBS 표준 FM",
        "channelId": "822",
        "channelType": "4",
        "broadcastTime": "1410",
        "channelEngName": "cbsfm"
      },
      {
        "programId": "1537",
        "imageSrc": "http://cfile189.uf.daum.net/image/235CC23953313B1F213D6C",
        "programMasterName": "김C의 뮤직쇼",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "1600",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "368",
        "imageSrc": "http://cfile190.uf.daum.net/image/21090838533254A122CB54",
        "programMasterName": "김창렬의 올드스쿨",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "1600",
        "channelEngName": "sbspw"
      }
    ]
  },
  {
    "items": [
      {
        "programId": "1377",
        "imageSrc": "http://cfile186.uf.daum.net/image/2563353A533254DF281504",
        "programMasterName": "케이윌의 영스트리트",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "2000",
        "channelEngName": "sbspw"
      },
      {
        "programId": "21",
        "imageSrc": "http://cfile139.uf.daum.net/image/2733573B53352232075D05",
        "programMasterName": "최양락의 재미있는 라디오",
        "description": "",
        "channelName": "MBC표준FM",
        "channelId": "832",
        "channelType": "4",
        "broadcastTime": "2025",
        "channelEngName": "mbcfm"
      },
      {
        "programId": "1632",
        "imageSrc": "http://cfile178.uf.daum.net/image/266493495355C2781FCC85",
        "programMasterName": "타블로와 꿈꾸는 라디오",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "2200",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "1425",
        "imageSrc": "http://cfile176.uf.daum.net/image/2575D236533254CB0922AE",
        "programMasterName": "장기하의 대단한 라디오",
        "description": "",
        "channelName": "SBS 파워 FM",
        "channelId": "835",
        "channelType": "4",
        "broadcastTime": "2200",
        "channelEngName": "sbspw"
      }
    ]
  }
]'''

tag6=u'''[
  {
    "items": [
      {
        "programId": "1371",
        "imageSrc": "http://cfile177.uf.daum.net/image/273E874D532AB48806DE34",
        "programMasterName": "나얼의 음악세계",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "0200",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "1585",
        "imageSrc": "http://cfile88.uf.daum.net/image/23704D3C533253C31C45DB",
        "programMasterName": "김범도의 새벽다방",
        "description": "",
        "channelName": "MBC표준FM",
        "channelId": "832",
        "channelType": "4",
        "broadcastTime": "0400",
        "channelEngName": "mbcfm"
      },
      {
        "programId": "643",
        "imageSrc": "http://cfile88.uf.daum.net/image/2660C8365406931815F187",
        "programMasterName": "그대와 여는 아침 김용신입니다",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "0700",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "250",
        "imageSrc": "http://cfile181.uf.daum.net/image/257844335332538C0D25EE",
        "programMasterName": "이루마의 골든디스크",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "1100",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "1594",
        "imageSrc": "http://cfile139.uf.daum.net/image/26603A4F532AB3B70FCC7E",
        "programMasterName": "최다니엘의 팝스팝스",
        "description": "",
        "channelName": "KBS 쿨 FM",
        "channelId": "826",
        "channelType": "4",
        "broadcastTime": "1100",
        "channelEngName": "kbs2fm"
      },
      {
        "programId": "750",
        "imageSrc": "http://cfile37.uf.daum.net/image/25556B4C532AB2FE2487D1",
        "programMasterName": "FM POPS 한동준입니다",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "1400",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "296",
        "imageSrc": "http://cfile189.uf.daum.net/image/256C274B532AB32D0D367E",
        "programMasterName": "배미향의 저녁스케치",
        "description": "",
        "channelName": "CBS 음악 FM",
        "channelId": "821",
        "channelType": "4",
        "broadcastTime": "1800",
        "channelEngName": "cbsmusicfm"
      },
      {
        "programId": "254",
        "imageSrc": "http://cfile104.uf.daum.net/image/210B6E4653313FA92F6C7B",
        "programMasterName": "배철수의 음악캠프",
        "description": "",
        "channelName": "MBC FM4U",
        "channelId": "831",
        "channelType": "4",
        "broadcastTime": "1800",
        "channelEngName": "mbcfm4u"
      },
      {
        "programId": "1580",
        "imageSrc": "http://cfile180.uf.daum.net/image/2248C9365332543E1C7816",
        "programMasterName": "박은경의 스위트 뮤직 박스",
        "description": "",
        "channelName": "SBS 러브 FM",
        "channelId": "834",
        "channelType": "4",
        "broadcastTime": "2030",
        "channelEngName": "sbslove"
      }
    ]
  }
]'''

tag2=json.loads(tag2)
tag9=json.loads(tag9)
tag6=json.loads(tag6) 
tags=[tag2,tag9,tag6]

class radio:
	def __init__(self):
		self.query_url='http://music.daum.net/onair/programScheduleSongList.json?searchDate=%(date)s&channelId=%(channelId)s&mediaType=4&programId=%(programId)s'
		self.prgoram_list=[]
		for tag in tags:
			for items in tag:
				programs=items['items']
				for program in programs:
					self.prgoram_list.append(program)

	def get_song_list(self,date):
		ret=[]
		for program in self.prgoram_list:
			print program['programMasterName']
			program['date']=date
			html=urllib2.urlopen(self.query_url%program).read()
			js=json.loads(html)
			#q='INSERT INTO songlist (,,,,,,) VALUES(:date,:channelId,:programId,:programMasterName,:channelName,:title,:artistName)'
			for song in js['songList']:
				d={}
				d['title']=song['title']
				d['artistName']=song['artistName']
				d['broadcastTime']=program['broadcastTime']
				d['channelId']=program['channelId']
				d['date']=program['date']
				d['programId']=program['programId']
				d['programMasterName']=program['programMasterName']
				d['channelName']=program['channelName']
				d['youtube']=youtube_search(d['title']+' '+d['artistName'])[1]
				ret.append(d)
		self.song_list=ret

	def insert_song_list(self):
		db=dbtool('radio.db')
		while self.song_list:
			song=self.song_list.pop()
			try:
				db.insert_song(song)
			except HTTPException:
				pass
			#except:
				#print '[!]error'
				#print repr(song)


if not os.path.isfile('radio.db'):
	radiodb_init()

r=radio()
try:
	date=sys.argv[1]
except:
	yesterday=datetime.date.today()-datetime.timedelta(days=1)
	date='%d%d%d'%(yesterday.year,yesterday.month,yesterday.day)

print 'start get song list %s'%date
r.get_song_list(date)
print 'end get song list'
print 'start db insert'
r.insert_song_list()
print 'end db insert'