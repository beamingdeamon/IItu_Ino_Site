<template>
    <div class="wrapper" id="main">
      <div class="animate__animated animate__bounceInLeft left_handler">
        <div class="title">
          <div class="main_title">IITU<br></div>
          <div class="second_title">INNOVATION<br></div>
          <div class="second_title">CENTER</div>
        </div>
        <div class="text">
          Функциональное <span class="bold">инновационное</span> пространство <span class="bold">с обустроенными рабочими местами, переговорным комнатам и игровой зоной.</span>
        </div>
        <a href="https://forms.gle/UyRUsqQyCFc252ea6" class="register">Оставить заявку</a>
      </div>
      <div class="animate__animated animate__bounceInRight right_handler">
        <div class="squares">
          <div class="radiant">
              <div class="opacity_block">
              Место глобально<br>мыслящих<br>профессионалов
            </div>
          </div>
          
        </div>
      </div>
    </div>
</template>

<script>
import 'animate.css'
export default {
  name:"Mainblock"
}
</script>

<style lang="sass" scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap')
  @font-face 
    font-family: 'Gilroy'
    src: local('Gilroy Bold'), local('Gilroy-Bold'), url('../assets/Gilroy/Gilroy-Bold.woff2') format('woff2'), url('../assets/Gilroy/Gilroy-Bold.woff') format('woff'), url('../assets/Gilroy/Gilroy-Bold.ttf') format('truetype')
    font-weight: 700
    font-style: normal

  .wrapper
    background-color: #12111A
    width: 100vw
    height: 100vh
    color: #FFFFFF
    display: flex
    flex-direction: row
    .right_handler
      width: 54vw
      height: 100vh
      .squares
        width: 83%
        height: 80% 
        float: right
        background: url("../assets/squares.png")
        .radiant
          width: 24%
          height: 28%
          margin-top: 25vh
          margin-left: 12vw
          background: no-repeat url("../assets/radiant.png")
          background-size: cover
          background-position: center center
          .opacity_block
            font-family: "Gilroy"
            font-weight: 600
            width: 28vw
            height: 17vh
            padding: 1.5vw
            margin-left: 5.5vw
            border-radius: 30px 0px 0px 30px
            background: rgba(255, 255, 255, 0.1)
            backdrop-filter: blur(10px)
            font-size: 2.2em
            line-height: 1.3
    .left_handler
      display: flex
      flex-direction: column
      align-items: center
      justify-content: center
      width: 46vw
      height: 100vh
      font-family: 'Montserrat', sans-serif
      .title
        width: 68%
        height: 27%
        margin-left: 7.5vw
        .main_title
          font-weight: 700
          font-size: 4em
        .second_title
          margin-top: 1.2vh
          font-weight: 400
          font-size: 3.3em
          letter-spacing: 3.5px
      .text
        margin-left: 7.5vw
        margin-top: 6vh
        font-size: 1.2em
        font-weight: regular
        width: 68%
        .bold
          font-weight: 600
      .register
        margin-right: 7.5vw
        margin-top: 4.5vh
        text-decoration: none
        font-weight: 700
        font-size: 1.2em
        background-color: white
        border-radius: 10px
        width: 35%
        text-align: center
        height: 6%
        color: black
        line-height: 2.5
  @media screen and ( max-width: 1024px )
    .wrapper
      background: url('../assets/first_block_mobile_bg.png') !important
      flex-direction: column !important
      .right_handler
        height: 40%
        width: 100% !important
        order: 1
        .squares
          background: none !important
          margin-left: 0 !important
          float: left !important
          .radiant
            margin-top: 47% !important
            background: none !important
            margin-left: 0 !important
            .opacity_block
              padding-top: 2vh !important
              padding-bottom: 2vh !important
              padding-left: 5vh !important
              font-family: 'Montserrat', sans-serif !important
              margin-left: 0 !important
              height: 12vh !important
              line-height: 1.7 !important
              font-size: 1.5em !important
              font-weight: 200 !important
              width: 70vw !important
              backdrop-filter: blur(10px) !important
              border-radius: 0px 30px 30px 0px !important
      .left_handler
        order: 2
        width: 100% !important
        .title
          width: 90% !important
          .main_title
            font-size: 3.4em !important
          .second_title 
            width: 100% !important
        .text
          margin-left: -13vw !important
        .register
          margin-top: 2vh !important
          margin-right: 26vw !important
          height: 8% !important
          width: 55% !important
          line-height: 6vh !important
</style>
