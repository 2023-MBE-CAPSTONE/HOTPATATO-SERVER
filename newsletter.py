from flask import Flask, render_template

app = Flask(__name__)

generated_article = {
    'issue_date': '20231101', 
    'negative_article': "이 이슈에 대해 반대하는 사람들의 의견을 들어보자고.\n\n반대하는 사람들이 많아. 왜냐하면, 의대 정원 확대는 의사들의 파업을 초래할 수 있거든.\n\n파업이라는 말을 들으면 무서워지지? 의사들이 파업을 하면, 우리가 받는 의료 서비스에 큰 영향을 미칠 수 있어.\n\n그리고 피부과라는 이야기도 있어. 의대 정원 확대가 이루어지면, 피부과와 같은 고수익 의료진들만 늘어날 수 있다는 거야. 이 이슈에 대해 어떻게 생각해?", 
    'positive_article': "알고 있겠지만, 이건 참 중요한 이야기거든.\n\n찬성하는 사람들이 많아. 왜냐하면, 의대 정원 확대는 의사 수를 늘려서 우리나라 의료 서비스를 더 좋게 만들 수 있거든.\n\n특권이라는 말도 많이 들어봤을 거야. 의사들이 특권을 가지고 있다는 사람들이 많아. 그래서 이런 사람들은 의대 정원 확대를 찬성해.\n\n그리고 이기적이라는 이야기도 있어. 의사들이 이기적이라고 생각하는 사람들이 많아. 그래서 이런 사람들은 의대 정원 확대를 찬성해. 이 이슈에 대해 어떻게 생각해?", 
    'issue_name': '의대 정원 확대', 
    'issue_article_title': "의대 정원 확대 논쟁: 의사 부족 해소 vs 의료계 우려",
}
positive_subtopic_list = [
	{
		"subtopic_article_name":"OECD 비교에서 의대 정원 확대 필요성 부각" ,
		 "subtopic_article": "국내 의대 정원이 오랜 시간 동안 고정돼 있어서 문제가 되고 있어.\n 그리고 OECD 국가들과 비교했을 때, 의사 수와 의대 정원이 부족한 게 밝혀져 있어. 그래서 다른 나라들은 의대 정원을 늘리고 있는데, 그렇게 하지 않으면 고령화에 대비하기가 어려워질 거야. 의료계에서는 의대 정원 확대에 반대 의견도 있지만, 여론 조사에서는 의대 정원을 늘려야 한다는 찬성 의견이 많이 나오고 있어. 이러한 맥락에서 의대 정원을 확대하는 방향으로 나아가야 할 필요가 있겠지." ,
		"subtopic_news_title_list": [
		"[더뉴스] 17년 째 고정 한국 의대 정원, OECD '꼴찌 수준'...다른 나라는?",
		"늘어나는 의대 정원, 의사 태부족 지방 중심 배정될 전망"
		]
	},
	{
			"subtopic_article_name":"민주당 의원, 의대 정원 확대를 긍정적으로 지지" ,
			 "subtopic_article": "민주당 의원이 의대 정원 확대를 지지하며 윤석열 대통령의 계획을 칭찬하는 긍정적 입장을 표명했어. 정성호 의원은 이 확대가 역대 정부에서 시도하지 못했던 엄청난 일이라고 언급했고, 무능한 정권에서 나온 좋은 일로 보았어. 또한, 공공의료 확대 방안을 보완하고 국민 지지를 얻을 것을 희망했어. 이에 대한 기대가 커지면서 의대 정원 확대에 대한 파업 가능성도 언급되었어. 정부와 여당은 이 문제를 신중하게 검토하고 있으며, 현재 국내 의대 정원은 2006년 이후로 고정돼 있어서 이에 대한 조치가 필요하다는 의견도 있지만, 구체적인 내용은 아직 밝혀지지 않았어.." ,
			"subtopic_news_title_list": [
			"민주당 의원, 이례적 尹 칭찬 '文정부도 겁먹고 못한 엄청난 일'",
			]
		}
]
negative_subtopic_list = [
	{
		"subtopic_article_name":"의대 증원 사실상 확정 의협 '총력 대응'" ,
		 "subtopic_article": "정부와 여당은 의대 증원을 강력하게 확정하려는데, 의사들과 의사 단체는 이에 반발하고 있어. 의사들은 확대 규모에 문제가 있고, 일방적인 확대는 의료계와의 신뢰를 저버릴 것으로 생각하고 있어. 이로 인해 의료계와 정부 간에 논란이 지속되고 있어." ,
		"subtopic_news_title_list": [
		"'확고한 신념' 의대 증원 사실상 확정 의협 '총력 대응'",
		"1,000명? 3,000명? 의대정원 확대 임박 의사단체 '강력 대응'"
		]
	},
	{
		"subtopic_article_name":"의대정원 확대' 또 막아선 의사협회" ,
		 "subtopic_article": "의사협회와 의사단체가 정부의 의대 정원 확대 계획에 강하게 반발하고 있어. 정부가 의대 정원을 일방적으로 확대하려고 하며, 의사들을 배제하고 있다는 주장이 나오고 있어. 의사협회와 의사단체는 합의된 절차와 수순을 따라야 한다고 주장하며, 협의체에서 의대 정원과 같은 현안을 결정해야 한다고 주장하고 있어. 이로 인해 의료현안과 관련한 논의가 재개되고, 정부는 2025학년도부터 의대 정원을 대폭 늘릴 계획을 가지고 있어." ,
		"subtopic_news_title_list": [
		"의대 정원 1천 명 이상 늘릴 듯' 전국 의대마다 증원",
		"'의대정원 확대' 또 막아선 의사협회"
		]
	}
]
issue_date_receive = generated_article["issue_date"]
issue_title_receive = generated_article['issue_article_title']
pos_article = generated_article['positive_article']
pos_subtopic_1_name = positive_subtopic_list[0]['subtopic_article_name']
pos_subtopic_1_article = positive_subtopic_list[0]['subtopic_article']
pos_subtopic_1_newstitle = positive_subtopic_list[0]['subtopic_news_title_list'][0]
pos_subtopic_1_newsurl = 'https://www.msn.com/ko-kr/news/other/%EB%8D%94%EB%89%B4%EC%8A%A4-17%EB%85%84-%EC%A7%B8-%EA%B3%A0%EC%A0%95-%ED%95%9C%EA%B5%AD-%EC%9D%98%EB%8C%80-%EC%A0%95%EC%9B%90-oecd-%EA%BC%B4%EC%B0%8C-%EC%88%98%EC%A4%80-%EB%8B%A4%EB%A5%B8-%EB%82%98%EB%9D%BC%EB%8A%94-ytn/vi-AA1igQvu'
pos_subtopic_1_newstitle_2 = positive_subtopic_list[0]['subtopic_news_title_list'][1]
pos_subtopic_1_newsurl_2 = 'https://m.kmib.co.kr/view_amp.asp?arcid=0924325354'
neg_article = generated_article['negative_article']
neg_subtopic_1_name = negative_subtopic_list[0]['subtopic_article_name']
neg_subtopic_1_article = negative_subtopic_list[0]['subtopic_article']
neg_subtopic_1_newstitle = negative_subtopic_list[0]['subtopic_news_title_list'][0]
neg_subtopic_1_newsurl = 'https://www.msn.com/ko-kr/news/other/%EB%8D%94%EB%89%B4%EC%8A%A4-17%EB%85%84-%EC%A7%B8-%EA%B3%A0%EC%A0%95-%ED%95%9C%EA%B5%AD-%EC%9D%98%EB%8C%80-%EC%A0%95%EC%9B%90-oecd-%EA%BC%B4%EC%B0%8C-%EC%88%98%EC%A4%80-%EB%8B%A4%EB%A5%B8-%EB%82%98%EB%9D%BC%EB%8A%94-ytn/vi-AA1igQvu'
neg_subtopic_1_newstitle_2 = negative_subtopic_list[0]['subtopic_news_title_list'][1]
neg_subtopic_1_newsurl_2 = 'https://m.kmib.co.kr/view_amp.asp?arcid=0924325354'

@app.route('/')
def related_article():
    return render_template('newsletter.html', 
                           issue_date_receive=issue_date_receive,
                           issue_title_receive=issue_title_receive,
                           pos_article=pos_article,
                           neg_article=neg_article,
                           pos_subtopic_1_name=pos_subtopic_1_name,
                           pos_subtopic_1_article=pos_subtopic_1_article,
                           pos_subtopic_1_newstitle=pos_subtopic_1_newstitle,
                           pos_subtopic_1_newsurl=pos_subtopic_1_newsurl,
                           pos_subtopic_1_newstitle_2=pos_subtopic_1_newstitle_2,
                           pos_subtopic_1_newsurl_2=pos_subtopic_1_newsurl_2,
                           neg_subtopic_1_name=neg_subtopic_1_name,
                           neg_subtopic_1_article=neg_subtopic_1_article,
                           neg_subtopic_1_newstitle=neg_subtopic_1_newstitle,
                           neg_subtopic_1_newsurl=neg_subtopic_1_newsurl,
                           neg_subtopic_1_newstitle_2=neg_subtopic_1_newstitle_2,
                           neg_subtopic_1_newsurl_2=neg_subtopic_1_newsurl_2

                           )

if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
