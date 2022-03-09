<template>
  <div class="wrapper">
    <div class="header">
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
    .header
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
          
</style>
