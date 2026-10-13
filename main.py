
import streamlit as st
import html

# =========================================
# 1. 페이지 설정
# =========================================
st.set_page_config(
    page_title="나의 단짝 포켓몬 찾기",
    page_icon="🌼",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================
# 2. MBTI별 포켓몬 데이터
# =========================================
POKEMON = {
    "INTJ": {
        "name": "뮤츠", "en": "Mewtwo", "id": 150,
        "types": "에스퍼",
        "feature": "뛰어난 지능과 독립적인 사고를 지닌 전설의 포켓몬",
        "reason": "깊이 생각하고 자신만의 길을 개척하는 INTJ와 잘 어울려요. 서로의 독립성을 존중하면서 중요한 순간에는 최고의 전략을 세울 수 있어요."
    },
    "INTP": {
        "name": "메타몽", "en": "Ditto", "id": 132,
        "types": "노말",
        "feature": "다른 포켓몬으로 자유롭게 변신할 수 있는 호기심 많은 포켓몬",
        "reason": "새로운 가능성을 탐구하는 INTP처럼 메타몽은 변화와 실험을 즐겨요. 엉뚱한 상상과 기발한 아이디어를 나누는 재미있는 단짝이 될 거예요."
    },
    "ENTJ": {
        "name": "리자몽", "en": "Charizard", "id": 6,
        "types": "불꽃 · 비행",
        "feature": "강한 자신감과 뜨거운 열정을 지닌 포켓몬",
        "reason": "목표를 향해 과감하게 나아가는 ENTJ와 리자몽은 에너지가 잘 맞아요. 어려운 도전도 함께 돌파하며 서로의 성장을 이끌어 줄 수 있어요."
    },
    "ENTP": {
        "name": "팬텀", "en": "Gengar", "id": 94,
        "types": "고스트 · 독",
        "feature": "장난기와 재치를 지닌 신비로운 포켓몬",
        "reason": "재치 있는 대화와 새로운 자극을 좋아하는 ENTP에게 잘 어울려요. 예상 밖의 장난과 기발한 발상으로 매일을 지루할 틈 없이 만들어 줄 거예요."
    },
    "INFJ": {
        "name": "가디안", "en": "Gardevoir", "id": 282,
        "types": "에스퍼 · 페어리",
        "feature": "소중한 사람을 지키려는 마음이 깊은 포켓몬",
        "reason": "상대의 마음을 세심하게 살피는 INFJ와 따뜻한 가디안은 닮은 점이 많아요. 말하지 않아도 서로의 마음을 헤아리는 다정한 단짝이 될 수 있어요."
    },
    "INFP": {
        "name": "이브이", "en": "Eevee", "id": 133,
        "types": "노말",
        "feature": "무한한 가능성과 사랑스러운 매력을 지닌 포켓몬",
        "reason": "자신만의 세계와 가능성을 소중히 여기는 INFP와 잘 어울려요. 서로의 개성을 있는 그대로 받아들이며 함께 꿈을 키워 갈 수 있어요."
    },
    "ENFJ": {
        "name": "피카츄", "en": "Pikachu", "id": 25,
        "types": "전기",
        "feature": "밝은 에너지와 강한 우정으로 동료에게 힘을 주는 포켓몬",
        "reason": "주변 사람들에게 긍정적인 에너지를 전하는 ENFJ와 찰떡궁합이에요. 힘든 날에는 서로를 응원하고 즐거운 날에는 기쁨을 두 배로 만들어 줄 거예요."
    },
    "ENFP": {
        "name": "토게피", "en": "Togepi", "id": 175,
        "types": "페어리",
        "feature": "행복과 기쁨을 상징하는 작고 사랑스러운 포켓몬",
        "reason": "호기심이 많고 새로운 경험을 즐기는 ENFP에게 토게피는 귀여운 행운의 친구예요. 평범한 하루도 작은 모험과 행복으로 가득 채워 줄 거예요."
    },
    "ISTJ": {
        "name": "이상해씨", "en": "Bulbasaur", "id": 1,
        "types": "풀 · 독",
        "feature": "차분하고 믿음직스러우며 꾸준히 성장하는 포켓몬",
        "reason": "책임감 있고 성실한 ISTJ에게 이상해씨는 든든한 파트너예요. 서두르지 않고 한 걸음씩 나아가며 오래도록 신뢰를 쌓을 수 있어요."
    },
    "ISFJ": {
        "name": "푸린", "en": "Jigglypuff", "id": 39,
        "types": "노말 · 페어리",
        "feature": "노래로 주변을 편안하게 해 주는 사랑스러운 포켓몬",
        "reason": "다른 사람을 살뜰히 챙기는 ISFJ와 푸린은 따뜻한 분위기가 잘 맞아요. 지친 하루가 끝나면 편안한 노래와 다정한 곁으로 마음을 쉬게 해 줄 거예요."
    },
    "ESTJ": {
        "name": "윈디", "en": "Arcanine", "id": 59,
        "types": "불꽃",
        "feature": "용감하고 충성심이 강한 포켓몬",
        "reason": "책임감 있게 팀을 이끄는 ESTJ에게 윈디는 믿음직한 동료예요. 어떤 상황에서도 서로를 믿고 목표를 향해 힘차게 달려갈 수 있어요."
    },
    "ESFJ": {
        "name": "파치리스", "en": "Pachirisu", "id": 417,
        "types": "전기",
        "feature": "활발하고 친근하며 주변에 활력을 전하는 포켓몬",
        "reason": "사람들과 어울리고 따뜻한 관계를 만드는 ESFJ와 잘 어울려요. 작은 배려와 즐거운 순간을 함께 나누며 주변까지 밝게 만들어 줄 거예요."
    },
    "ISTP": {
        "name": "루카리오", "en": "Lucario", "id": 448,
        "types": "격투 · 강철",
        "feature": "침착하고 뛰어난 감각으로 상황을 파악하는 포켓몬",
        "reason": "실용적이고 문제 해결에 강한 ISTP와 루카리오는 멋진 콤비예요. 위기에서도 침착하게 방법을 찾아내고 말보다 행동으로 믿음을 보여 줄 거예요."
    },
    "ISFP": {
        "name": "치코리타", "en": "Chikorita", "id": 152,
        "types": "풀",
        "feature": "온화하고 다정하며 자연을 좋아하는 포켓몬",
        "reason": "자신만의 감성과 아름다움을 소중히 여기는 ISFP에게 치코리타는 포근한 친구예요. 자연 속을 산책하고 소소한 행복을 발견하며 편안한 시간을 보낼 수 있어요."
    },
    "ESTP": {
        "name": "갸라도스", "en": "Gyarados", "id": 130,
        "types": "물 · 비행",
        "feature": "압도적인 힘과 대담함을 지닌 강력한 포켓몬",
        "reason": "망설이기보다 직접 도전하는 ESTP와 갸라도스는 넘치는 에너지가 닮았어요. 스릴 넘치는 모험도 두려워하지 않고 함께 새로운 한계를 넘어설 수 있어요."
    },
    "ESFP": {
        "name": "에브이", "en": "Espeon", "id": 196,
        "types": "에스퍼",
        "feature": "우아하고 영리하며 소중한 친구를 잘 따르는 포켓몬",
        "reason": "밝고 매력적이며 현재의 즐거움을 만끽하는 ESFP에게 에브이는 특별한 친구예요. 서로의 감각과 매력을 나누며 일상 속 반짝이는 순간을 만들어 줄 거예요."
    },
}

# =========================================
# 3. CSS 디자인
# 중요: CSS 전체를 삼중 따옴표로 감싸기
# =========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gowun+Dodum&display=swap');

:root {
    --cream: #FFF9E9;
    --butter: #FFE69A;
    --yellow: #F6C64A;
    --brown: #59452D;
    --soft: #927754;
}

.stApp {
    background-color: var(--cream);
    color: var(--brown);
}

html, body, [class*="css"] {
    font-family: 'Gowun Dodum', sans-serif;
}

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
    color: var(--brown) !important;
}

.hero {
    background: #FFFEFA;
    border: 2px solid #F4DFA8;
    border-radius: 30px;
    padding: 30px 18px;
    text-align: center;
    box-shadow: 0 10px 30px #8B6D3010;
}

.hero-icon {
    font-size: 3rem;
}

.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: clamp(2rem, 6vw, 3rem);
    margin: 12px 0;
    color: #59452D;
    line-height: 1.35;
}

.hero-desc {
    color: #927754;
    font-size: 1.1rem;
    line-height: 1.9;
}

.tag {
    display: inline-block;
    background: #FFF0BC;
    border-radius: 30px;
    padding: 7px 14px;
    color: #805C17;
}

.result-card {
    background: #FFFEFA;
    border: 2px solid #F2D580;
    border-radius: 28px;
    padding: 24px 16px;
    text-align: center;
    box-shadow: 0 12px 30px #8B6D3010;
}

.result-name {
    font-family: 'Jua', sans-serif;
    font-size: clamp(2rem, 6vw, 3rem);
    margin: 10px 0;
}

.result-sub {
    color: #927754;
    font-size: 1rem;
}

.info-box {
    background: #FFFEFA;
    border: 1px solid #F1E0B8;
    border-radius: 20px;
    padding: 18px 20px;
    margin-top: 14px;
    line-height: 1.9;
    font-size: 1.04rem;
}

.info-title {
    font-family: 'Jua', sans-serif;
    color: #795B2D;
    font-size: 1.25rem;
    margin-bottom: 6px;
}

.type-chip {
    display: inline-block;
    background: #FFF0BC;
    border: 1px solid #F0D58B;
    border-radius: 30px;
    padding: 7px 14px;
    margin: 5px;
    color: #775719;
    font-weight: bold;
}

.stButton > button {
    background: linear-gradient(135deg, #FFE69A, #F6C64A);
    color: #59452D;
    border: none;
    border-radius: 17px;
    min-height: 56px;
    font-family: 'Jua', sans-serif;
    font-size: 1.2rem;
    box-shadow: 0 4px 0 #D9A934;
}

.stButton > button:hover {
    background: #FFDE7B;
    color: #59452D;
    border: none;
}

div[data-baseweb="select"] > div {
    background: #FFFEFA;
    border: 2px solid #F1D99A;
    border-radius: 14px;
    min-height: 50px;
}

.stSelectbox label {
    color: #59452D !important;
    font-weight: bold !important;
    font-size: 1.05rem !important;
}

.footer {
    text-align: center;
    color: #A18B68;
    font-size: .9rem;
    line-height: 1.8;
    padding-top: 25px;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .hero {
        padding: 24px 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 4. 제목과 소개
# =========================================
st.markdown("""
<div class="hero">
    <div class="hero-icon">🌼 ⚡ 🌼</div>
    <div class="tag">MY MBTI × POKÉMON</div>
    <div class="hero-title">나의 단짝 포켓몬 찾기!</div>
    <div class="hero-desc">
        나와 가장 잘 어울리는 포켓몬은 누구일까요?<br>
        나의 MBTI를 고르고 운명의 단짝을 만나 보세요 💛
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================
# 5. MBTI 선택
# =========================================
MBTI_LABELS = {
    "INTJ": "INTJ · 전략가",
    "INTP": "INTP · 논리적인 사색가",
    "ENTJ": "ENTJ · 대담한 통솔자",
    "ENTP": "ENTP · 변론가",
    "INFJ": "INFJ · 선의의 옹호자",
    "INFP": "INFP · 열정적인 중재자",
    "ENFJ": "ENFJ · 정의로운 사회운동가",
    "ENFP": "ENFP · 재기발랄한 활동가",
    "ISTJ": "ISTJ · 청렴결백한 논리주의자",
    "ISFJ": "ISFJ · 용감한 수호자",
    "ESTJ": "ESTJ · 엄격한 관리자",
    "ESFJ": "ESFJ · 사교적인 외교관",
    "ISTP": "ISTP · 만능 재주꾼",
    "ISFP": "ISFP · 호기심 많은 예술가",
    "ESTP": "ESTP · 모험을 즐기는 사업가",
    "ESFP": "ESFP · 자유로운 영혼의 연예인",
}

MBTI_LIST = list(MBTI_LABELS.keys())

st.markdown(
    '<div class="info-title">🌷 STEP 1. 나의 MBTI를 선택해 주세요!</div>',
    unsafe_allow_html=True,
)

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = "INFP"

if "found_mbti" not in st.session_state:
    st.session_state.found_mbti = None

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

selected = st.selectbox(
    "나의 MBTI 유형",
    MBTI_LIST,
    format_func=lambda value: MBTI_LABELS[value],
    index=MBTI_LIST.index(st.session_state.selected_mbti),
    key="mbti_selector",
)

st.caption("💡 가장 나와 비슷하다고 느끼는 유형을 골라도 괜찮아요!")

# =========================================
# 6. 단짝 포켓몬 찾기
# =========================================
if st.button("✨ 내 단짝 포켓몬 찾기!", use_container_width=True):
    st.session_state.selected_mbti = selected
    st.session_state.found_mbti = selected
    st.session_state.celebrate = True

# =========================================
# 7. 결과 표시
# =========================================
result_mbti = st.session_state.found_mbti

if result_mbti:
    pokemon = POKEMON[result_mbti]

    st.markdown("---")
    st.markdown(
        '<div class="info-title">🎉 STEP 2. 운명의 단짝을 만났어요!</div>',
        unsafe_allow_html=True,
    )

    if st.session_state.celebrate:
        st.balloons()
        st.snow()
        st.session_state.celebrate = False

    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-size:1.15rem;">💛 축하해요! 나의 단짝 포켓몬은 💛</div>
            <div class="result-name">{html.escape(pokemon["name"])}</div>
            <div class="result-sub">
                {html.escape(pokemon["en"])} · 도감 번호 No. {pokemon["id"]:04d}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 포켓몬 공식 아트워크 이미지 URL
    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        "sprites/pokemon/other/official-artwork/"
        + str(pokemon["id"])
        + ".png"
    )

    st.image(
        image_url,
        use_container_width=True,
        caption=f'{pokemon["name"]} ({pokemon["en"]})',
    )

    st.markdown(
        f"""
        <div style="text-align:center; margin:15px 0;">
            <span class="type-chip">⚡ 타입: {html.escape(pokemon["types"])}</span>
            <span class="type-chip">💫 MBTI: {result_mbti}</span>
        </div>
        <div class="info-box">
            <div class="info-title">🌟 포켓몬의 특징</div>
            {html.escape(pokemon["feature"])}
        </div>
        <div class="info-box">
            <div class="info-title">💌 우리가 단짝인 이유</div>
            {html.escape(pokemon["reason"])}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.success(
        f'🎊 {result_mbti}와 {pokemon["name"]}의 단짝 매칭 완료!'
    )

    if st.button("🔄 다른 MBTI로 다시 찾기", use_container_width=True):
        st.session_state.found_mbti = None
        st.session_state.celebrate = False
        st.rerun()

else:
    st.markdown("""
    <div class="info-box" style="text-align:center; margin-top:20px;">
        <div style="font-size:2.5rem;">🥚</div>
        <div class="info-title">포켓몬 알이 기다리고 있어요!</div>
        MBTI를 선택하고 노란색 버튼을 누르면<br>
        나만의 특별한 단짝 포켓몬이 나타나요.
    </div>
    """, unsafe_allow_html=True)

# =========================================
# 8. 하단 안내
# =========================================
st.markdown("""
<div class="footer">
    🌼 너와 포켓몬에게 행복한 하루가 되길! 🌼<br>
    MBTI 매칭은 재미를 위해 만든 콘텐츠입니다.<br>
    포켓몬 이미지 제공: PokeAPI GitHub 이미지 저장소<br>
    이미지를 표시하려면 인터넷 연결이 필요합니다.
</div>
""", unsafe_allow_html=True)
import streamlit as st
import html

# =========================================
# 1. 페이지 설정
# =========================================
st.set_page_config(
    page_title="나의 단짝 포켓몬 찾기",
    page_icon="🌼",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================
# 2. MBTI별 포켓몬 데이터
# =========================================
POKEMON = {
    "INTJ": {
        "name": "뮤츠", "en": "Mewtwo", "id": 150,
        "types": "에스퍼",
        "feature": "뛰어난 지능과 독립적인 사고를 지닌 전설의 포켓몬",
        "reason": "깊이 생각하고 자신만의 길을 개척하는 INTJ와 잘 어울려요. 서로의 독립성을 존중하면서 중요한 순간에는 최고의 전략을 세울 수 있어요."
    },
    "INTP": {
        "name": "메타몽", "en": "Ditto", "id": 132,
        "types": "노말",
        "feature": "다른 포켓몬으로 자유롭게 변신할 수 있는 호기심 많은 포켓몬",
        "reason": "새로운 가능성을 탐구하는 INTP처럼 메타몽은 변화와 실험을 즐겨요. 엉뚱한 상상과 기발한 아이디어를 나누는 재미있는 단짝이 될 거예요."
    },
    "ENTJ": {
        "name": "리자몽", "en": "Charizard", "id": 6,
        "types": "불꽃 · 비행",
        "feature": "강한 자신감과 뜨거운 열정을 지닌 포켓몬",
        "reason": "목표를 향해 과감하게 나아가는 ENTJ와 리자몽은 에너지가 잘 맞아요. 어려운 도전도 함께 돌파하며 서로의 성장을 이끌어 줄 수 있어요."
    },
    "ENTP": {
        "name": "팬텀", "en": "Gengar", "id": 94,
        "types": "고스트 · 독",
        "feature": "장난기와 재치를 지닌 신비로운 포켓몬",
        "reason": "재치 있는 대화와 새로운 자극을 좋아하는 ENTP에게 잘 어울려요. 예상 밖의 장난과 기발한 발상으로 매일을 지루할 틈 없이 만들어 줄 거예요."
    },
    "INFJ": {
        "name": "가디안", "en": "Gardevoir", "id": 282,
        "types": "에스퍼 · 페어리",
        "feature": "소중한 사람을 지키려는 마음이 깊은 포켓몬",
        "reason": "상대의 마음을 세심하게 살피는 INFJ와 따뜻한 가디안은 닮은 점이 많아요. 말하지 않아도 서로의 마음을 헤아리는 다정한 단짝이 될 수 있어요."
    },
    "INFP": {
        "name": "이브이", "en": "Eevee", "id": 133,
        "types": "노말",
        "feature": "무한한 가능성과 사랑스러운 매력을 지닌 포켓몬",
        "reason": "자신만의 세계와 가능성을 소중히 여기는 INFP와 잘 어울려요. 서로의 개성을 있는 그대로 받아들이며 함께 꿈을 키워 갈 수 있어요."
    },
    "ENFJ": {
        "name": "피카츄", "en": "Pikachu", "id": 25,
        "types": "전기",
        "feature": "밝은 에너지와 강한 우정으로 동료에게 힘을 주는 포켓몬",
        "reason": "주변 사람들에게 긍정적인 에너지를 전하는 ENFJ와 찰떡궁합이에요. 힘든 날에는 서로를 응원하고 즐거운 날에는 기쁨을 두 배로 만들어 줄 거예요."
    },
    "ENFP": {
        "name": "토게피", "en": "Togepi", "id": 175,
        "types": "페어리",
        "feature": "행복과 기쁨을 상징하는 작고 사랑스러운 포켓몬",
        "reason": "호기심이 많고 새로운 경험을 즐기는 ENFP에게 토게피는 귀여운 행운의 친구예요. 평범한 하루도 작은 모험과 행복으로 가득 채워 줄 거예요."
    },
    "ISTJ": {
        "name": "이상해씨", "en": "Bulbasaur", "id": 1,
        "types": "풀 · 독",
        "feature": "차분하고 믿음직스러우며 꾸준히 성장하는 포켓몬",
        "reason": "책임감 있고 성실한 ISTJ에게 이상해씨는 든든한 파트너예요. 서두르지 않고 한 걸음씩 나아가며 오래도록 신뢰를 쌓을 수 있어요."
    },
    "ISFJ": {
        "name": "푸린", "en": "Jigglypuff", "id": 39,
        "types": "노말 · 페어리",
        "feature": "노래로 주변을 편안하게 해 주는 사랑스러운 포켓몬",
        "reason": "다른 사람을 살뜰히 챙기는 ISFJ와 푸린은 따뜻한 분위기가 잘 맞아요. 지친 하루가 끝나면 편안한 노래와 다정한 곁으로 마음을 쉬게 해 줄 거예요."
    },
    "ESTJ": {
        "name": "윈디", "en": "Arcanine", "id": 59,
        "types": "불꽃",
        "feature": "용감하고 충성심이 강한 포켓몬",
        "reason": "책임감 있게 팀을 이끄는 ESTJ에게 윈디는 믿음직한 동료예요. 어떤 상황에서도 서로를 믿고 목표를 향해 힘차게 달려갈 수 있어요."
    },
    "ESFJ": {
        "name": "파치리스", "en": "Pachirisu", "id": 417,
        "types": "전기",
        "feature": "활발하고 친근하며 주변에 활력을 전하는 포켓몬",
        "reason": "사람들과 어울리고 따뜻한 관계를 만드는 ESFJ와 잘 어울려요. 작은 배려와 즐거운 순간을 함께 나누며 주변까지 밝게 만들어 줄 거예요."
    },
    "ISTP": {
        "name": "루카리오", "en": "Lucario", "id": 448,
        "types": "격투 · 강철",
        "feature": "침착하고 뛰어난 감각으로 상황을 파악하는 포켓몬",
        "reason": "실용적이고 문제 해결에 강한 ISTP와 루카리오는 멋진 콤비예요. 위기에서도 침착하게 방법을 찾아내고 말보다 행동으로 믿음을 보여 줄 거예요."
    },
    "ISFP": {
        "name": "치코리타", "en": "Chikorita", "id": 152,
        "types": "풀",
        "feature": "온화하고 다정하며 자연을 좋아하는 포켓몬",
        "reason": "자신만의 감성과 아름다움을 소중히 여기는 ISFP에게 치코리타는 포근한 친구예요. 자연 속을 산책하고 소소한 행복을 발견하며 편안한 시간을 보낼 수 있어요."
    },
    "ESTP": {
        "name": "갸라도스", "en": "Gyarados", "id": 130,
        "types": "물 · 비행",
        "feature": "압도적인 힘과 대담함을 지닌 강력한 포켓몬",
        "reason": "망설이기보다 직접 도전하는 ESTP와 갸라도스는 넘치는 에너지가 닮았어요. 스릴 넘치는 모험도 두려워하지 않고 함께 새로운 한계를 넘어설 수 있어요."
    },
    "ESFP": {
        "name": "에브이", "en": "Espeon", "id": 196,
        "types": "에스퍼",
        "feature": "우아하고 영리하며 소중한 친구를 잘 따르는 포켓몬",
        "reason": "밝고 매력적이며 현재의 즐거움을 만끽하는 ESFP에게 에브이는 특별한 친구예요. 서로의 감각과 매력을 나누며 일상 속 반짝이는 순간을 만들어 줄 거예요."
    },
}

# =========================================
# 3. CSS 디자인
# 중요: CSS 전체를 삼중 따옴표로 감싸기
# =========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gowun+Dodum&display=swap');

:root {
    --cream: #FFF9E9;
    --butter: #FFE69A;
    --yellow: #F6C64A;
    --brown: #59452D;
    --soft: #927754;
}

.stApp {
    background-color: var(--cream);
    color: var(--brown);
}

html, body, [class*="css"] {
    font-family: 'Gowun Dodum', sans-serif;
}

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
    color: var(--brown) !important;
}

.hero {
    background: #FFFEFA;
    border: 2px solid #F4DFA8;
    border-radius: 30px;
    padding: 30px 18px;
    text-align: center;
    box-shadow: 0 10px 30px #8B6D3010;
}

.hero-icon {
    font-size: 3rem;
}

.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: clamp(2rem, 6vw, 3rem);
    margin: 12px 0;
    color: #59452D;
    line-height: 1.35;
}

.hero-desc {
    color: #927754;
    font-size: 1.1rem;
    line-height: 1.9;
}

.tag {
    display: inline-block;
    background: #FFF0BC;
    border-radius: 30px;
    padding: 7px 14px;
    color: #805C17;
}

.result-card {
    background: #FFFEFA;
    border: 2px solid #F2D580;
    border-radius: 28px;
    padding: 24px 16px;
    text-align: center;
    box-shadow: 0 12px 30px #8B6D3010;
}

.result-name {
    font-family: 'Jua', sans-serif;
    font-size: clamp(2rem, 6vw, 3rem);
    margin: 10px 0;
}

.result-sub {
    color: #927754;
    font-size: 1rem;
}

.info-box {
    background: #FFFEFA;
    border: 1px solid #F1E0B8;
    border-radius: 20px;
    padding: 18px 20px;
    margin-top: 14px;
    line-height: 1.9;
    font-size: 1.04rem;
}

.info-title {
    font-family: 'Jua', sans-serif;
    color: #795B2D;
    font-size: 1.25rem;
    margin-bottom: 6px;
}

.type-chip {
    display: inline-block;
    background: #FFF0BC;
    border: 1px solid #F0D58B;
    border-radius: 30px;
    padding: 7px 14px;
    margin: 5px;
    color: #775719;
    font-weight: bold;
}

.stButton > button {
    background: linear-gradient(135deg, #FFE69A, #F6C64A);
    color: #59452D;
    border: none;
    border-radius: 17px;
    min-height: 56px;
    font-family: 'Jua', sans-serif;
    font-size: 1.2rem;
    box-shadow: 0 4px 0 #D9A934;
}

.stButton > button:hover {
    background: #FFDE7B;
    color: #59452D;
    border: none;
}

div[data-baseweb="select"] > div {
    background: #FFFEFA;
    border: 2px solid #F1D99A;
    border-radius: 14px;
    min-height: 50px;
}

.stSelectbox label {
    color: #59452D !important;
    font-weight: bold !important;
    font-size: 1.05rem !important;
}

.footer {
    text-align: center;
    color: #A18B68;
    font-size: .9rem;
    line-height: 1.8;
    padding-top: 25px;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .hero {
        padding: 24px 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 4. 제목과 소개
# =========================================
st.markdown("""
<div class="hero">
    <div class="hero-icon">🌼 ⚡ 🌼</div>
    <div class="tag">MY MBTI × POKÉMON</div>
    <div class="hero-title">나의 단짝 포켓몬 찾기!</div>
    <div class="hero-desc">
        나와 가장 잘 어울리는 포켓몬은 누구일까요?<br>
        나의 MBTI를 고르고 운명의 단짝을 만나 보세요 💛
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================
# 5. MBTI 선택
# =========================================
MBTI_LABELS = {
    "INTJ": "INTJ · 전략가",
    "INTP": "INTP · 논리적인 사색가",
    "ENTJ": "ENTJ · 대담한 통솔자",
    "ENTP": "ENTP · 변론가",
    "INFJ": "INFJ · 선의의 옹호자",
    "INFP": "INFP · 열정적인 중재자",
    "ENFJ": "ENFJ · 정의로운 사회운동가",
    "ENFP": "ENFP · 재기발랄한 활동가",
    "ISTJ": "ISTJ · 청렴결백한 논리주의자",
    "ISFJ": "ISFJ · 용감한 수호자",
    "ESTJ": "ESTJ · 엄격한 관리자",
    "ESFJ": "ESFJ · 사교적인 외교관",
    "ISTP": "ISTP · 만능 재주꾼",
    "ISFP": "ISFP · 호기심 많은 예술가",
    "ESTP": "ESTP · 모험을 즐기는 사업가",
    "ESFP": "ESFP · 자유로운 영혼의 연예인",
}

MBTI_LIST = list(MBTI_LABELS.keys())

st.markdown(
    '<div class="info-title">🌷 STEP 1. 나의 MBTI를 선택해 주세요!</div>',
    unsafe_allow_html=True,
)

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = "INFP"

if "found_mbti" not in st.session_state:
    st.session_state.found_mbti = None

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

selected = st.selectbox(
    "나의 MBTI 유형",
    MBTI_LIST,
    format_func=lambda value: MBTI_LABELS[value],
    index=MBTI_LIST.index(st.session_state.selected_mbti),
    key="mbti_selector",
)

st.caption("💡 가장 나와 비슷하다고 느끼는 유형을 골라도 괜찮아요!")

# =========================================
# 6. 단짝 포켓몬 찾기
# =========================================
if st.button("✨ 내 단짝 포켓몬 찾기!", use_container_width=True):
    st.session_state.selected_mbti = selected
    st.session_state.found_mbti = selected
    st.session_state.celebrate = True

# =========================================
# 7. 결과 표시
# =========================================
result_mbti = st.session_state.found_mbti

if result_mbti:
    pokemon = POKEMON[result_mbti]

    st.markdown("---")
    st.markdown(
        '<div class="info-title">🎉 STEP 2. 운명의 단짝을 만났어요!</div>',
        unsafe_allow_html=True,
    )

    if st.session_state.celebrate:
        st.balloons()
        st.snow()
        st.session_state.celebrate = False

    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-size:1.15rem;">💛 축하해요! 나의 단짝 포켓몬은 💛</div>
            <div class="result-name">{html.escape(pokemon["name"])}</div>
            <div class="result-sub">
                {html.escape(pokemon["en"])} · 도감 번호 No. {pokemon["id"]:04d}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 포켓몬 공식 아트워크 이미지 URL
    image_url = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        "sprites/pokemon/other/official-artwork/"
        + str(pokemon["id"])
        + ".png"
    )

    st.image(
        image_url,
        use_container_width=True,
        caption=f'{pokemon["name"]} ({pokemon["en"]})',
    )

    st.markdown(
        f"""
        <div style="text-align:center; margin:15px 0;">
            <span class="type-chip">⚡ 타입: {html.escape(pokemon["types"])}</span>
            <span class="type-chip">💫 MBTI: {result_mbti}</span>
        </div>
        <div class="info-box">
            <div class="info-title">🌟 포켓몬의 특징</div>
            {html.escape(pokemon["feature"])}
        </div>
        <div class="info-box">
            <div class="info-title">💌 우리가 단짝인 이유</div>
            {html.escape(pokemon["reason"])}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.success(
        f'🎊 {result_mbti}와 {pokemon["name"]}의 단짝 매칭 완료!'
    )

    if st.button("🔄 다른 MBTI로 다시 찾기", use_container_width=True):
        st.session_state.found_mbti = None
        st.session_state.celebrate = False
        st.rerun()

else:
    st.markdown("""
    <div class="info-box" style="text-align:center; margin-top:20px;">
        <div style="font-size:2.5rem;">🥚</div>
        <div class="info-title">포켓몬 알이 기다리고 있어요!</div>
        MBTI를 선택하고 노란색 버튼을 누르면<br>
        나만의 특별한 단짝 포켓몬이 나타나요.
    </div>
    """, unsafe_allow_html=True)

# =========================================
# 8. 하단 안내
# =========================================
st.markdown("""
<div class="footer">
    🌼 너와 포켓몬에게 행복한 하루가 되길! 🌼<br>
    MBTI 매칭은 재미를 위해 만든 콘텐츠입니다.<br>
    포켓몬 이미지 제공: PokeAPI GitHub 이미지 저장소<br>
    이미지를 표시하려면 인터넷 연결이 필요합니다.
</div>
""", unsafe_allow_html=True)
