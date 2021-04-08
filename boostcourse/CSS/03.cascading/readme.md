#### cascading

CSS는 여러가지 스타일 정보를 기반으로 최종적으로 '경쟁'에 의해서 적절한 스타일이 반영된다.



선언방식에 따른 차이



#### inline이 최우선, 그 다음 internal 그 다음 external



``` css
body > span {
	color : red;
}

span {
	color : blue;
}
```

이렇게 좀더 지엽적인 상대를 지정한 것이 우선 적용됨(마치 레이아웃 깔듯이)





``` css
span {
	color : red;
}

span {
	color : blue;
}
```

이렇게 지정하는 곳이 같을 경우에는 맨 마지막 설정을 따른다.(오류 안남)





``` html
<div id = "a", class ="b">
	text...
</div>
```



``` css
#a {
	color : red;
}

.b {
	color : blue;
}
```

#id 가 .class 보다 우선권이 높다. (점수를 많이 받음) 그래서 붉은색이 출력.



#### id이 최우선, 그 다음 class 그 다음 element