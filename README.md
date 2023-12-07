# LLM 기반 균형 있는 사회 이슈 뉴스레터 서비스 - 뜨거운 감자
## 프로젝트 소개

2023 뉴스빅데이터 해커톤에서 사회 양극화 문제를 해결할 뉴스레터 서비스를 개발하여 최우수상을 수상

## 아키텍쳐
<img width="795" alt="image" src="https://github.com/2023-MBE-CAPSTONE/HOTPATATO-SERVER/assets/79091824/263775d1-e90f-4e63-8d4d-054114d1732f">

## 레포지토리 구조
```
HOTPOTATO-SERVER
├── .github/workflows
│   ├── generate_newsletter.yml
│   └── send_newsletter.yml
├── api
│   └── user.py
├── dynamodb
│   ├── generated_articles.py
│   ├── generated_newsletters.py
│   ├── issue_keywords.py
│   └── users.py
├── models
│   ├── generated_article.py
│   ├── generated_newsletter.py
│   ├── issue_keyword.py
│   └── user.py
├── scripts
│   ├── generate_newsletter.py
│   └── send_newsletter.py
├── service
│   └── user_service.py
├── utils
│   ├── util.py
│   └── date.py
├── .gitignore
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── app.py
├── chain.py
├── requirements.txt
└── README.md 
```
