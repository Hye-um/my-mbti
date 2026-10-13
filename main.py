```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBTI 포켓몬 찾기</title>

  <style>
    * {
      box-sizing: border-box;
    }

    :root {
      --cream: #fff9e9;
      --yellow: #ffdc70;
      --yellow-dark: #f2c34e;
      --brown: #51432e;
      --muted: #82745e;
      --white: #ffffff;
    }

    body {
      margin: 0;
      min-height: 100vh;
      padding: 32px 16px 56px;
      background: var(--cream);
      color: var(--brown);
      font-family:
        "Malgun Gothic", "Apple SD Gothic Neo",
        "Noto Sans KR", sans-serif;
    }

    button {
      font: inherit;
    }

    .container {
      width: 100%;
      max-width: 900px;
      margin: 0 auto;
    }

    header {
      text-align: center;
      margin-bottom: 30px;
    }

    .eyebrow {
      display: inline-block;
      padding: 8px 14px;
      border-radius: 999px;
      background: #fff0b9;
      font-size: 14px;
      font-weight: 800;
      margin-bottom: 12px;
    }

    h1 {
      margin: 0;
      font-size: clamp(30px, 6vw, 46px);
      letter-spacing: -1.8px;
      line-height: 1.25;
    }

    .subtitle {
      margin: 14px 0 0;
      color: var(--muted);
      font-size: 17px;
      line-height: 1.7;
    }

    .section-title {
      margin: 26px 0 14px;
      font-size: 21px;
      font-weight: 900;
    }

    .mbti-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 10px;
    }

    .mbti-button {
      min-height: 58px;
      padding: 12px 6px;
      border: 2px solid #f2e6c9;
      border-radius: 15px;
      background: var(--white);
      color: var(--brown);
      font-size: 18px;
      font-weight: 900;
      cursor: pointer;
      transition: transform 0.15s, background 0.15s,
                  border-color 0.15s;
    }

    .mbti-button:hover {
      transform: translateY(-2px);
      border-color: var(--yellow-dark);
    }

    .mbti-button.active {
      background: var(--yellow);
      border-color: var(--yellow-dark);
    }

    .result {
      display: none;
      margin-top: 30px;
      padding: 26px;
      border: 2px solid #f2e6c9;
      border-radius: 26px;
      background: var(--white);
      box-shadow: 0 12px 35px rgba(95, 73, 30, 0.07);
      animation: appear 0.25s ease-out;
    }

    .result.show {
      display: block;
    }

    @keyframes appear {
      from {
        opacity: 0;
        transform: translateY(8px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .result-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 12px;
    }

    .type-label {
      padding: 8px 13px;
      border-radius: 999px;
      background: #fff0b9;
      font-size: 15px;
      font-weight: 900;
    }

    .result-number {
      color: var(--muted);
      font-size: 14px;
      font-weight: 700;
    }

    .pokemon-area {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 8px 0 18px;
    }

    .image-frame {
      display: flex;
      align-items: center;
      justify-content: center;
      width: min(100%, 300px);
      height: 260px;
      margin: 0 auto 12px;
      overflow: hidden;
      border-radius: 22px;
      background:
        radial-gradient(circle, #fff0b9 0%, #fff9e9 68%);
    }

    .pokemon-image {
      display: none;
      width: 100%;
      height: 100%;
      padding: 12px;
      object-fit: contain;
    }

    .image-placeholder {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 20px;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.6;
    }

    .placeholder-emoji {
      font-size: 64px;
    }

    .image-placeholder strong {
      color: var(--brown);
      font-size: 17px;
    }

    .pokemon-name {
      margin: 4px 0 5px;
      font-size: clamp(28px, 5vw, 36px);
      font-weight: 1000;
      letter-spacing: -1px;
    }

    .pokemon-english {
      color: var(--muted);
      font-size: 15px;
      font-weight: 700;
    }

    .description {
      margin-top: 12px;
      padding: 20px;
      border-radius: 18px;
      background: #fff9e9;
    }

    .description h3,
    .compatibility h3 {
      margin: 0 0 10px;
      font-size: 18px;
    }

    .description p {
      margin: 0;
      font-size: 16px;
      line-height: 1.9;
      white-space: pre-line;
      word-break: keep-all;
    }

    .compatibility {
      margin-top: 16px;
      padding: 20px;
      border: 2px dashed #efd58d;
      border-radius: 18px;
    }

    .compatible-type {
      display: inline-block;
      padding: 9px 14px;
      border-radius: 999px;
      background: var(--yellow);
      font-size: 17px;
      font-weight: 900;
    }

    .compatible-note {
      margin: 10px 0 0;
      color: var(--muted);
      font-size: 15px;
      line-height: 1.7;
    }

    .reset-wrap {
      display: flex;
      justify-content: center;
      margin-top: 22px;
    }

    .reset-button {
      padding: 13px 22px;
      border: 0;
      border-radius: 14px;
      background: #eee5d2;
      color: var(--brown);
      font-size: 16px;
      font-weight: 900;
      cursor: pointer;
    }

    .reset-button:hover {
      background: #e5d8bd;
    }

    .footer-note {
      margin: 25px 0 0;
      text-align: center;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.7;
    }

    @media (max-width: 520px) {
      body {
        padding: 24px 12px 40px;
      }

      .mbti-grid {
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 7px;
      }

      .mbti-button {
        min-height: 52px;
        font-size: 16px;
        border-radius: 12px;
      }

      .result {
        padding: 17px;
        border-radius: 20px;
      }

      .image-frame {
        height: 230px;
      }

      .description,
      .compatibility {
        padding: 16px;
      }
    }
  </style>
</head>

<body>
  <main class="container">
    <header>
      <div class="eyebrow">⚡ MY POKÉMON PARTNER</div>
      <h1>MBTI로 포켓몬 찾기</h1>
      <p class="subtitle">
        내 성격과 찰떡인 포켓몬은 누구일까?<br>
        아래에서 내 MBTI를 선택해 봐!
      </p>
    </header>

    <section aria-labelledby="choose-title">
      <h2 class="section-title" id="choose-title">
        🌼 나의 MBTI를 선택해 줘
      </h2>

      <div class="mbti-grid" id="mbtiGrid"></div>
    </section>

    <section class="result" id="result" aria-live="polite">
      <div class="result-top">
        <span class="type-label" id="typeLabel"></span>
        <span class="result-number" id="resultNumber"></span>
      </div>

      <div class="pokemon-area">
        <div class="image-frame">
          <img
            class="pokemon-image"
            id="pokemonImage"
            alt=""
            referrerpolicy="no-referrer"
          >

          <div class="image-placeholder" id="imagePlaceholder">
            <span class="placeholder-emoji" id="placeholderEmoji">⚡</span>
            <strong id="placeholderName">포켓몬 이미지를 불러오는 중...</strong>
            <span id="placeholderMessage">잠시만 기다려 줘!</span>
          </div>
        </div>

        <h2 class="pokemon-name" id="pokemonName"></h2>
        <div class="pokemon-english" id="pokemonEnglish"></div>
      </div>

      <div class="description">
        <h3>💛 너와 닮은 이유</h3>
        <p id="descriptionText"></p>
      </div>

      <div class="compatibility">
        <h3>🤝 이런 MBTI와 잘 맞아요</h3>
        <span class="compatible-type" id="compatibleType"></span>
        <p class="compatible-note" id="compatibleNote"></p>
      </div>

      <div class="reset-wrap">
        <button class="reset-button" id="resetButton" type="button">
          ↻ 다시 선택하기
        </button>
      </div>
    </section>

    <p class="footer-note">
      포켓몬 매칭은 재미를 위한 성격 유형 테스트예요.<br>
      포켓몬 이미지는 인터넷 연결이 필요합니다.
    </p>
  </main>

  <script>
    const pokemonData = {
      ISTJ: {
        id: 9,
        name: "거북왕",
        english: "Blastoise",
        emoji: "🐢",
        compatible: "ESFP",
        reason:
          "책임감이 강하고 믿음직한 ISTJ!\n" +
          "거북왕처럼 차분하게 자기 역할을 해내고,\n" +
          "어려운 상황에서도 쉽게 흔들리지 않아요.",
        compatibleReason:
          "신중한 ISTJ와 활기찬 ESFP는 서로에게 없는 매력을 발견하고 일상에 균형을 더할 수 있어요."
      },

      ISFJ: {
        id: 242,
        name: "해피너스",
        english: "Blissey",
        emoji: "💗",
        compatible: "ESFP",
        reason:
          "다정하고 주변 사람을 잘 챙기는 ISFJ!\n" +
          "해피너스처럼 따뜻한 마음으로 친구를 돌보고,\n" +
          "작은 배려로 주변을 행복하게 만들어요.",
        compatibleReason:
          "따뜻한 ISFJ와 밝은 ESFP는 함께 즐거운 추억을 만들고 서로의 마음을 편안하게 해줄 수 있어요."
      },

      INFJ: {
        id: 282,
        name: "가디안",
        english: "Gardevoir",
        emoji: "✨",
        compatible: "ENFP",
        reason:
          "깊이 생각하고 사람의 마음을 잘 이해하는 INFJ!\n" +
          "가디안처럼 소중한 사람을 진심으로 지키며,\n" +
          "자신만의 따뜻한 신념을 가지고 있어요.",
        compatibleReason:
          "섬세한 INFJ와 자유로운 ENFP는 서로의 생각을 넓혀 주며 깊은 유대감을 만들 수 있어요."
      },

      INTJ: {
        id: 150,
        name: "뮤츠",
        english: "Mewtwo",
        emoji: "🧠",
        compatible: "ENFP",
        reason:
          "분석적이고 독립적인 전략가 INTJ!\n" +
          "뮤츠처럼 목표를 향해 깊이 고민하고,\n" +
          "자신만의 방식으로 해결책을 찾아가요.",
        compatibleReason:
          "계획적인 INTJ와 아이디어가 넘치는 ENFP는 서로의 관점을 넓히고 새로운 가능성을 발견할 수 있어요."
      },

      ISTP: {
        id: 376,
        name: "메타그로스",
        english: "Metagross",
        emoji: "⚙️",
        compatible: "ESFJ",
        reason:
          "문제를 빠르게 파악하고 실전에 강한 ISTP!\n" +
          "메타그로스처럼 논리적으로 분석하고,\n" +
          "필요한 순간에 침착하게 행동해요.",
        compatibleReason:
          "실용적인 ISTP와 사람을 잘 챙기는 ESFJ는 서로의 부족한 부분을 보완할 수 있어요."
      },

      ISFP: {
        id: 133,
        name: "이브이",
        english: "Eevee",
        emoji: "🦊",
        compatible: "ENFJ",
        reason:
          "자기만의 감성과 부드러운 매력을 가진 ISFP!\n" +
          "이브이처럼 다양한 가능성을 품고 있으며,\n" +
          "좋아하는 것을 자신만의 방식으로 표현해요.",
        compatibleReason:
          "자유로운 ISFP와 따뜻한 ENFJ는 서로의 개성을 존중하면서 함께 성장할 수 있어요."
      },

      INFP: {
        id: 39,
        name: "푸린",
        english: "Jigglypuff",
        emoji: "🎤",
        compatible: "ENFJ",
        reason:
          "상상력이 풍부하고 마음이 따뜻한 INFP!\n" +
          "푸린처럼 자신만의 감성과 꿈을 소중히 여기며,\n" +
          "진심을 담아 주변 사람에게 다가가요.",
        compatibleReason:
          "이상적인 INFP와 적극적인 ENFJ는 서로의 꿈을 응원하며 따뜻한 관계를 만들어 갈 수 있어요."
      },

      INTP: {
        id: 65,
        name: "후딘",
        english: "Alakazam",
        emoji: "🔮",
        compatible: "ENTJ",
        reason:
          "호기심이 많고 논리적으로 생각하는 INTP!\n" +
          "후딘처럼 궁금한 것을 깊이 탐구하고,\n" +
          "남들이 놓친 새로운 관점을 찾아내요.",
        compatibleReason:
          "아이디어가 풍부한 INTP와 실행력이 강한 ENTJ는 생각을 실제 성과로 발전시킬 수 있어요."
      },

      ESTP: {
        id: 6,
        name: "리자몽",
        english: "Charizard",
        emoji: "🔥",
        compatible: "ISFJ",
        reason:
          "대담하고 행동력이 넘치는 ESTP!\n" +
          "리자몽처럼 도전을 두려워하지 않고,\n" +
          "눈앞의 기회를 재빠르게 잡아내요.",
        compatibleReason:
          "활동적인 ESTP와 세심한 ISFJ는 서로에게 새로운 경험과 안정감을 선물할 수 있어요."
      },

      ESFP: {
        id: 25,
        name: "피카츄",
        english: "Pikachu",
        emoji: "⚡",
        compatible: "ISTJ",
        reason:
          "밝고 에너지가 넘치는 분위기 메이커 ESFP!\n" +
          "피카츄처럼 친근한 매력으로 사람들을 웃게 하고,\n" +
          "지금 이 순간을 즐기는 데 능숙해요.",
        compatibleReason:
          "밝고 즉흥적인 ESFP와 차분하고 계획적인 ISTJ는 서로에게 색다른 시각을 더해 줄 수 있어요."
      },

      ENFP: {
        id: 175,
        name: "토게피",
        english: "Togepi",
        emoji: "🥚",
        compatible: "INFJ",
        reason:
          "새로운 가능성을 발견하는 걸 좋아하는 ENFP!\n" +
          "토게피처럼 사랑스럽고 긍정적인 에너지로\n" +
          "주변에 설렘과 즐거움을 퍼뜨려요.",
        compatibleReason:
          "활발한 ENFP와 깊이 있는 INFJ는 서로의 상상력과 생각을 자극하며 특별한 관계를 만들 수 있어요."
      },

      ENTP: {
        id: 94,
        name: "팬텀",
        english: "Gengar",
        emoji: "👻",
        compatible: "INTJ",
        reason:
          "재치 있고 새로운 아이디어를 좋아하는 ENTP!\n" +
          "팬텀처럼 장난기와 독특한 매력을 지녔으며,\n" +
          "뻔한 방식보다 색다른 해결책을 즐겨 찾아요.",
        compatibleReason:
          "아이디어가 넘치는 ENTP와 전략적인 INTJ는 서로의 생각을 발전시키고 큰 그림을 그릴 수 있어요."
      },

      ESTJ: {
        id: 68,
        name: "괴력몬",
        english: "Machamp",
        emoji: "💪",
        compatible: "ISFP",
        reason:
          "결단력이 있고 책임감이 강한 ESTJ!\n" +
          "괴력몬처럼 목표를 향해 힘차게 나아가고,\n" +
          "팀을 이끌며 일을 확실하게 마무리해요.",
        compatibleReason:
          "체계적인 ESTJ와 유연한 ISFP는 서로 다른 강점을 인정하면서 균형 잡힌 관계를 만들 수 있어요."
      },

      ESFJ: {
        id: 40,
        name: "푸크린",
        english: "Wigglytuff",
        emoji: "🎈",
        compatible: "ISTP",
        reason:
          "사람들과 어울리는 걸 좋아하고 정이 많은 ESFJ!\n" +
          "푸크린처럼 다정하고 친근하게 다가가며,\n" +
          "모두가 함께 즐길 수 있는 분위기를 만들어요.",
        compatibleReason:
          "사람 중심의 ESFJ와 독립적인 ISTP는 서로의 다른 성향을 이해하며 새로운 균형을 찾을 수 있어요."
      },

      ENFJ: {
        id: 448,
        name: "루카리오",
        english: "Lucario",
        emoji: "🥋",
        compatible: "INFP",
        reason:
          "사람을 응원하고 이끄는 힘이 있는 ENFJ!\n" +
          "루카리오처럼 동료를 소중히 여기고,\n" +
          "자신의 신념을 행동으로 보여 줘요.",
        compatibleReason:
          "사람을 이끄는 ENFJ와 진심을 중시하는 INFP는 서로의 가치관을 이해하며 함께 성장할 수 있어요."
      },

      ENTJ: {
        id: 373,
        name: "보만다",
        english: "Salamence",
        emoji: "🐉",
        compatible: "INTP",
        reason:
          "큰 목표를 세우고 추진하는 리더 ENTJ!\n" +
          "보만다처럼 더 높은 곳을 향해 도전하고,\n" +
          "계획을 세워 결과를 만들어 내는 데 강해요.",
        compatibleReason:
          "추진력이 있는 ENTJ와 분석적인 INTP는 전략과 아이디어를 결합해 큰 목표에 도전할 수 있어요."
      }
    };

    const mbtiOrder = [
      "ISTJ", "ISFJ", "INFJ", "INTJ",
      "ISTP", "ISFP", "INFP", "INTP",
      "ESTP", "ESFP", "ENFP", "ENTP",
      "ESTJ", "ESFJ", "ENFJ", "ENTJ"
    ];

    const mbtiGrid = document.getElementById("mbtiGrid");
    const result = document.getElementById("result");
    const pokemonImage = document.getElementById("pokemonImage");
    const imagePlaceholder = document.getElementById("imagePlaceholder");

    let currentType = null;
    let imageAttempt = 0;

    // MBTI 버튼 만들기
    mbtiOrder.forEach((type) => {
      const button = document.createElement("button");

      button.type = "button";
      button.className = "mbti-button";
      button.textContent = type;
      button.dataset.type = type;
      button.setAttribute("aria-label", type + " 포켓몬 결과 보기");

      button.addEventListener("click", () => showPokemon(type));

      mbtiGrid.appendChild(button);
    });

    function showPokemon(type) {
      const data = pokemonData[type];

      if (!data) return;

      currentType = type;

      document.querySelectorAll(".mbti-button").forEach((button) => {
        const selected = button.dataset.type === type;
        button.classList.toggle("active", selected);
        button.setAttribute("aria-pressed", String(selected));
      });

      document.getElementById("typeLabel").textContent =
        type + " 타입의 포켓몬";

      document.getElementById("resultNumber").textContent =
        "도감 번호 #" + String(data.id).padStart(3, "0");

      document.getElementById("pokemonName").textContent = data.name;
      document.getElementById("pokemonEnglish").textContent = data.english;
      document.getElementById("descriptionText").textContent = data.reason;

      document.getElementById("compatibleType").textContent =
        data.compatible;

      document.getElementById("compatibleNote").textContent =
        data.compatibleReason;

      // 이전 이미지 요청의 결과가 새 결과에 영향을 주지 않게 초기화
      imageAttempt++;
      const thisAttempt = imageAttempt;

      pokemonImage.onload = () => {
        if (thisAttempt !== imageAttempt) return;

        pokemonImage.style.display = "block";
        imagePlaceholder.style.display = "none";
      };

      pokemonImage.onerror = () => {
        if (thisAttempt !== imageAttempt) return;

        // 첫 번째 주소가 실패하면 PokéAPI 이미지 주소로 한 번 더 시도
        if (pokemonImage.dataset.source === "official") {
          pokemonImage.dataset.source = "pokeapi";

          pokemonImage.src =
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/" +
            data.id + ".png";

          return;
        }

        // 두 주소 모두 실패한 경우 대체 화면 표시
        pokemonImage.style.display = "none";
        imagePlaceholder.style.display = "flex";

        document.getElementById("placeholderEmoji").textContent =
          data.emoji;

        document.getElementById("placeholderName").textContent =
          data.name;

        document.getElementById("placeholderMessage").textContent =
          "이미지를 불러오지 못했어요. 인터넷 연결을 확인해 주세요.";
      };

      pokemonImage.alt = data.name + " (" + data.english + ") 공식 아트워크";
      pokemonImage.style.display = "none";
      imagePlaceholder.style.display = "flex";

      document.getElementById("placeholderEmoji").textContent = data.emoji;
      document.getElementById("placeholderName").textContent = data.name;
      document.getElementById("placeholderMessage").textContent =
        "포켓몬 이미지를 불러오는 중...";

      // 먼저 포켓몬 공식 도감 이미지 주소 사용
      pokemonImage.dataset.source = "official";
      pokemonImage.src =
        "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" +
        String(data.id).padStart(3, "0") + ".png";

      result.classList.add("show");

      result.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });
    }

    function resetPage() {
      currentType = null;
      imageAttempt++;

      result.classList.remove("show");

      document.querySelectorAll(".mbti-button").forEach((button) => {
        button.classList.remove("active");
        button.setAttribute("aria-pressed", "false");
      });

      pokemonImage.onload = null;
      pokemonImage.onerror = null;
      pokemonImage.removeAttribute("src");
      pokemonImage.style.display = "none";

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    }

    document.getElementById("resetButton").addEventListener("click", resetPage);
  </script>
</body>
</html>
```
