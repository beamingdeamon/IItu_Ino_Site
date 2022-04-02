<template>
  <div class="wrapper" id="fourth">
    <div class="fourth_header">
      <h1>Что внутри?</h1>
      <h2>У нас есть много классных вещей, которые <span class="bold_text">вы можете использовать абсолютно бесплатно</span></h2>
    </div>
    <div class="bot_block">
      <div class="bot_items_wrapper">
        <div class="bot_item">
          <div class="number">1</div>
          <div class="opacity"><h2>WIFI</h2></div>
        </div>
        <div class="bot_item">
          <div class="number">2</div>
          <div class="opacity"><h2>Чай и кофе</h2></div>
        </div>
        <div class="bot_item">
          <div class="number">3</div>
          <div class="opacity"><h2>Комнаты для<br> переговоров</h2></div>
        </div>
        <div class="bot_item">
          <div class="number">4</div>
          <div class="opacity"><h2>Индивидуальные места работы</h2></div>
        </div>
        <div class="bot_item">
          <div class="number">5</div>
          <div class="opacity"><h2>Оборудование</h2></div>
        </div>
        <div class="bot_item">
          <div class="number">6</div>
          <div class="opacity"><h2>Зона для<br>отдыха и игры</h2></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FourthBlock"
}
</script>

<style lang="sass" scoped>
  .wrapper
    width: 100vw
    height: 100vh
    background: url("../assets/fourth_block_bg.png")
    background-size: cover
    background-position: center center
    display: flex
    flex-direction: column
    align-items: center
    font-family: 'Montserrat', sans-serif
    color: white
    .fourth_header
      width: 87%
      height: 18vh
      h1
        margin-top: 10vh
        font-weight: 400
        font-size: 3.2em
        margin-bottom: 3vh
      h2
        font-weight: 400
        font-size: 1.1em
      .bold_text
        font-weight: 600
    .bot_block
      width: 100%
      height: 82vh
      .bot_items_wrapper
        margin-top: 10vh
        display: grid
        grid-template-columns: 1fr 1fr 1fr
        .bot_item
          width: 20vw
          height: 30vh
          margin-left: 6vw
          .number
            font-style: italic
            margin-left: 2vw
            font-weight: 500
            font-size: 8em
            transform: rotate(-3.06deg)
            background: radial-gradient( #FFFFFF 0%, #6D8DFF 100%)
            -webkit-background-clip: text
            -webkit-text-fill-color: transparent
          .opacity
            width: 90%
            background: rgba(255, 255, 255, 0.1)
            backdrop-filter: blur(10px)
            border-radius: 20px
            margin-top: -4vh
            padding-left: 1vw
            padding-right: 1vw
            height: 34%
            display: flex
            align-items: center
            h2
              margin-left: 1vw
              font-size: 1.2em
              font-weight: 400 
  @media screen and ( max-width: 1024px )
    .wrapper
      background: url('../assets/fourth_block_mobile_bg.png') !important
      height: 250vh !important
      .fourth_header
        h1
          margin-top: 9vh !important
        h2
          line-height: 2 !important
          font-size: 1.2em !important
      .bot_block
        height: 232vh !important
        .bot_items_wrapper
          margin-top: 15vh !important
          display: flex !important
          flex-direction: column !important
          align-items: center !important
          .bot_item
            margin-top: 4.5vh !important
            width: 90% !important
            height: 30vh !important
            margin-left: 0 !important
            .number
              margin-left: 13vw !important
              font-size: 15em !important
              transform: rotate(-3.06deg)
              background: radial-gradient( #FFFFFF 0%, #6D8DFF 100%)
              -webkit-background-clip: text
              -webkit-text-fill-color: transparent
            .opacity
              width: 90% !important
              height: 29% !important
              border-radius: 10px !important
              margin-top: -6vh !important
              padding-left: 6vw !important
              h2
                font-size: 1.6em !important
</style>
