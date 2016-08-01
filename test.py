# this is test page for beginning

# greeting = 'HI~ Hello~ Greeting!!~'
#
# print(greeting)

from htmldom import htmldom

# dom = htmldom.HtmlDom("http://m.naver.com").createDom()

# dom = htmldom.HtmlDom().createDom(
#     """
#
#     """
# )

dom = htmldom.HtmlDom().createDom("""<html lang="ko">
<body>
<section class="contentSection">
<!-- 컨텐츠 영역 -->
<article class="contentsArticle">
<article>
<div class="content_wrap">
<!-- 당첨번호 start -------------->
<div class="lotto_win_number mt12">
<p class="number">
<img src="/img/common/ball_2.png" alt="2"/>
<img src="/img/common/ball_5.png" alt="5"/>
<img src="/img/common/ball_15.png" alt="15"/>
<img src="/img/common/ball_18.png" alt="18"/>
<img src="/img/common/ball_19.png" alt="19"/>
<img src="/img/common/ball_23.png" alt="23"/>
</p>
<span class="hide">+</span>
<p class="number_bonus"><img src="/img/common/ball_44.png" alt="44"/></p>
</div>
<!-- 당첨번호 end -------------->

<!-- 순위 정보 start -------------->
<table class="tblType1 f12" summary="회차별 당첨번호 및 당첨금을 안내해드립니다.">
<thead>
<tr>
<th>순위</th>
<th device="pc">등위별 총 당첨금액</th>
<th>당첨게임 수</th>
<th>1게임당 당첨금액</th>
<th device="pc">당첨기준</th>
<th device="pc" class="tbbghn">비고</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" class="tblType1line1"></td>
</tr>
<tr>
<td><strong>1등</strong></td>
<td device="pc" class="rt"><strong>15,432,488,253원</strong></td>
<td class="rt">9</td>
<td class="rt">1,714,720,917원</td>
<td device="pc" class="rt pr30">당첨번호 <strong>6개</strong> 숫자일치</td>
<td device="pc" rowspan="5" class="tbbghn">
&nbsp;<br/>

1등<br />

자동6<br />


수동2<br />


반자동1


</td>
</tr>
<tr>
<td><strong>2등</strong></td>
<td device="pc" class="rt"><strong>2,572,081,400원</strong></td>
<td class="rt">50</td>
<td class="rt">51,441,628원</td>
<td device="pc" class="rt pr30">당첨번호 <strong>5개</strong> 숫자일치<br>+<strong>보너스</strong> 숫자일치</td>
</tr>
<tr>
<td><strong>3등</strong></td>
<td device="pc" class="rt"><strong>2,572,081,965원</strong></td>
<td class="rt">1,791</td>
<td class="rt">1,436,115원</td>
<td device="pc" class="rt pr30">당첨번호<strong>5개</strong> 숫자일치</td>
</tr>
<tr>
<td><strong>4등</strong></td>
<td device="pc" class="rt"><strong>4,396,000,000원</strong></td>
<td class="rt">87,920</td>
<td class="rt">50,000원</td>
<td device="pc" class="rt pr30">당첨번호 <strong>4개</strong> 숫자일치</td>
</tr>
<tr>
<td><strong>5등</strong></td>
<td device="pc" class="rt"><strong>7,350,625,000원</strong></td>
<td class="rt">1,470,125</td>
<td class="rt">5,000원</td>
<td device="pc" class="rt pr30">당첨번호 <strong>3개</strong> 숫자일치</td>
</tr>
<tr device="pc">
<td colspan="6" class="tblType1line1"></td>
</tr>
</tbody>
</table>
<!-- 순위 정보 end -------------->

<div class="mt20 over_h">
<ul class="fl">
<li><span>* 당첨금 지급기한 : 지급개시일로부터 1년 (휴일인 경우 익영업일)</span></li>
<li><span>* 총판매금액 : </span> <span class="f_blue">64,646,552,000원</span></li>
</ul>
</div></div></article></article>
</section>
</body>
</html>""")

# 당첨번호
pWin = dom.find("p").attr("class", "number")

for img in pWin.children():
    print(img.attr('alt'))

# 보너스 번호
# pBonus = dom.find("p").attr('class', 'number_bonus')

# print(pBonus.first().attr('alt'))

# print(p.first().html())




