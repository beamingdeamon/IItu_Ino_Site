<template>
    <div class="wrapper">
      <div class="animate__animated animate__bounceInLeft left_handler">
        <div class="title">
          <div class="main_title">IITU<br></div>
          <div class="second_title">INNOVATION<br></div>
          <div class="second_title">CENTER</div>
        </div>
        <div class="text">
          Функциональное <span class="bold">инновационное</span> пространство <span class="bold">с обустроенными рабочими местами, переговорным комнатам и игровой зоной.</span>
        </div>
        <a href="https://docs.google.com/forms/d/1LtJAvp_5nJUkYDsbvNpeQrVvk322_ioy1oQrW8rRwr0/viewform?edit_requested=true" class="register">Оставить заявку</a>
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
        width: 90%
        height: 80% 
        float: right
        background: url("../assets/squares.png")
        .radiant
          width: 20%
          height: 27%
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
        .main_title
          font-weight: 700
          font-size: 4em
        .second_title
          margin-top: 1.2vh
          font-weight: 400
          font-size: 3.3em
          letter-spacing: 3.5px
      .text
        margin-top: 6vh
        font-size: 1.2em
        font-weight: regular
        width: 68%
        .bold
          font-weight: 600
      .register
        margin-top: 4.5vh
        text-decoration: none
        font-size: 1.2em
        border: 1px solid grey
        border-radius: 30px
        width: 35%
        text-align: center
        height: 4.5%
        color: grey
        line-height: 1.8
  @media screen and ( max-width: 1024px )
      .right_handler
        display: none
      .left_handler
        width: 100% !important
        .title
          width: 80% !important
          .second_title 
            width: 80% !important
        .register
          width: 50% !important
          line-height: 2.3 !important
</style>
