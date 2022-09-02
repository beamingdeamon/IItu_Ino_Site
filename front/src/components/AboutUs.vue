<template>
  <div class="wrapper" id="about-us">
    <div class="about_line"></div>
    <div class="top_wrapper">
      <div class="left_handler ">
        <h1 class="h1">О нас</h1>
        <h2 class="h2"><span class="bold_aboutus">Наш центр</span> представляет собой творческое пространство, <span class="bold_aboutus">где будущие предприниматели могут работать над своими проектами</span>, обмениваться опытом, получать наставничество опытных бизнесменов и привлекать инвестирование на капитализацию своих бизнес-идей.</h2>
        <a href="https://www.instagram.com/itinocenter/?hl=ru" target="_blank"><img src="../assets/instagram.svg" alt="instagram">Подписаться</a>
      </div>
      <div class="right_handler ">
        <div class="first_image">
         <div class="second_image"></div>
        </div>
        
        <div class="about_circle"></div>
      </div>
    </div>
    <div class="bottom_handler">
        <div class="opacity_block">
          <div class="cube"></div>
          <h1 class="opacity_block_title">Для кого?</h1>
          <h2 class="opacity_block_text"><span class="bold_aboutus">В первую очередь для бизнеса завтрашнего дня - быстрорастущих инновационных компаний будущего, технологических проектов, направленных на глобальный рынок.</span> В общем, для всех тех, кто остро нуждается в правильной атмосфере, необходимой для продуктивной работы. Встречи с менторами и инвесторами, участие в конкурсах, хакатонах, буткампах, беседы с руководителями успешных стартапов помогут вам эффективно запустить свой проект</h2>
        </div>
        <div class="about_card"></div>
    </div>
  </div>
</template>

<script>
import 'animate.css'
export default {
  name:"AboutUs"
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
    width: 100vw
    height: 125vh
    display: flex
    flex-direction: column
    background-color: #12111A
    color: white
    font-family: 'Montserrat', sans-serif
    background: url("../assets/aboutus_block_bg.png")
    background-size: 100%
    background-position: center center
    .top_wrapper
      display: flex
      flex-direction: row
      width: 100vw
      height: 95vh
      .left_handler
        width: 40%
        height: 100%
        display: flex
        align-items: center
        flex-direction: column
        .h1
          margin-top: 10vh
          font-weight: 400
          font-size: 4em
          margin-left: 7vw
          width: 60%
          padding:0
          margin-bottom: 1vh
        .h2
          margin-left: 14.8vw
          font-weight: 400
          font-size: 1.2em
          width: 80%
          letter-spacing: 1.3px
          .bold_aboutus
            font-weight: 600
        a
          margin-top: 9vh
          color: black
          text-decoration: none
          font-family: 'Montserrat', sans-serif
          font-size: 1.1em
          display: flex
          align-items: center
          justify-content: center
          background-color: #FFFFFF
          font-weight: 600
          width: 35%
          margin-right: 3vw
          height: 8%
          border-radius: 10px
          img
            margin-right: 0.5vw
      .right_handler
        width: 60%
        height: 100%
        display: flex
        align-items: center
        .about_circle
          background: url("../assets/about_circle.png")
          background-size: cover
          background-position: center center
          position: absolute
          width: 40vw
          height: 80vh
          filter: blur(100px)
          margin-top: 36vh
          left: 48vw
          z-index: 0
        .first_image
          margin-top: 4vh
          z-index: 100
          margin-left: 29vw
          height: 68%
          width: 34%
          background: url("../assets/about_image1.png")
          background-size: cover
          background-position: center center
          border-radius: 20px
        .second_image
          width: 11%
          height: 22%
          position: absolute
          left: 85vw
          top: 108vh
          margin-bottom: 3vh
          border-radius: 30px
          background: url("../assets/about_image1.jpg")
          background-size: cover
          background-position: center center
    .bottom_handler
      width: 100vw
      height: 35vh
      font-family: "Gilroy"
      display: flex
      justify-content: center
      .about_card
        background: url("../assets/about_card.png")
        background-size: cover
        background-position: center center
        width: 9%
        height: 17%
        left: 2vw
        margin-top: 10vh
        position: absolute
        z-index: 0
      .opacity_block
        height: 75%
        width: 87%
        margin-top: 2vw
        border-radius: 30px
        background: rgba(255, 255, 255, 0.1)
        backdrop-filter: blur(10px)
        z-index: 100
        .opacity_block_title
          margin-left: 3vw
          margin-top: 4vh
          margin-bottom: 0
        .opacity_block_text
          margin-left: 3vw
          margin-top: 1vh
          font-family: 'Montserrat', sans-serif
          font-size: 0.9em
          line-height: 1.5
          font-weight: 400
          width: 80%
          .bold_aboutus
            font-weight: 700
        .cube
          background: url("../assets/about_cube.png")
          background-size: cover
          background-position: center center
          width: 6vw
          height: 10vh
          float: right
          position: absolute
          left: 84.5vw
          margin-top: -5vh
  @media screen and ( max-width: 1024px )
    .wrapper
      height: 210vh !important
      background: url('../assets/aboutus_block_mobile_bg.png')
      position: relative !important
      .top_wrapper
        display: flex
        flex-direction: column
        height: 130vh
        .left_handler
          width: 90% !important
          height: 65vh !important
          order: 2
          .h1
            position: absolute !important
            top: 4% !important
            margin-top: 0 !important
            font-weight: 400
            font-size: 4em
            left: 5% !important
            width: 60%
            padding:0
            margin-bottom: 1vh
          .h2
            font-size: 1.3em !important
            line-height: 1.5 !important
            width: 90% !important
            margin-left: 13vw !important
          a
            margin-top: 4vh !important
            width: 52vw !important
            height: 6vh !important
            font-size: 1.2em
            margin-right: 18vw !important
            img
              margin-right: 4.5vw !important
        .right_handler
          width: 100% !important
          height: 71% !important
          order: 1
          .first_image
            margin-top: 14vh !important
            width: 61vw
            height: 46vh
            border-radius: 10px !important
            margin-left: 12vw !important
          .second_image
            width: 37vw !important
            height: 17vh !important
            position: absolute
            left: 50vw !important
            top: 9% !important
            margin-bottom: 3vh !important
            margin-top: 0 !important
            border-radius: 10px !important
      .bottom_handler
        height: 80vh !important
        .about_card
          width: 35vw !important
          height: 20vh !important
          left: 0 !important
          margin-top: 60vh !important
        .opacity_block
          height: 85%
          width: 80% !important
          margin-top: 7vh !important
          border-radius: 20px !important
          backdrop-filter: blur(8px) !important
          .opacity_block_title
            margin-left: 5vw !important
            margin-top: 3vh !important
            font-size: 3em !important
          .opacity_block_text
            margin-left: 5vw !important
            margin-top: 2vh !important
            font-size: 1.15em !important
            line-height: 1.7 !important
            width: 85% !important
          .cube
            width: 16vw !important
            height: 10vh !important
            left: 82% !important
         
</style>
