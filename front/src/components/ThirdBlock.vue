<template>
  <div class="wrapper">
    <div class="header">Что мы предлогаем?</div>
    <div class="bot_handler">
      <div class="text_block">
        <h1>Программа акселерации</h1>
        <div class="white_line"></div>
        <h2>Программа акселерации - <span class="bold_text">это комплексная поддержка начинающих предпринимателей</span>, включающая в себя обучение, наставничество, и доступ к финансированию.</h2>
      </div>
      <div class="text_block">
        <h1>Консалтинг</h1>
        <div class="white_line"></div>
        <h2>Делимся опытом с корпоративными клиентами по работе со стартапами. <span class="bold_text">Мастер-классы для сотрудников по дизайн-мышлению. Проведение хакатонов, Startup Weekend.</span></h2>
      </div>
      <div class="text_block">
        <h1>Рабочее пространство</h1>
        <div class="white_line"></div>
        <h2><span class="bold_text">Коворкинг, офис и конференц-зал. Мероприятии</span> представляют собой площадки, <span class="bold_text">собирающие вместе стартапов, инвесторов</span>, корпорации и представителей государственных учреждений.</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:"ThirdBlock"
}
</script>

<style lang="sass" scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap')
  .wrapper
    width: 100vw
    height: 80vh
    background: url("../assets/third_block_bg.png")
    background-size: cover
    background-position: center center
    font-family: 'Montserrat', sans-serif
    display: flex
    flex-direction: column
    .header
      margin-left: 6vw
      margin-top: 15vh
      float: left
      font-size: 4em
      letter-spacing: 2.5px
    .bot_handler
      width: 100vw
      margin-top: 13vh
      display: flex
      flex-direction: row
      aling-items: center
      justify-content: space-evenly
      .text_block
        width: 24vw
        height: 24vh
        border-radius: 10px
        color: white
        padding: 1vw
        background: rgba(18, 17, 26, 0.7)
        backdrop-filter: blur(8px)
        h1
          margin-left: 1vw
          font-size: 1.3em
        .white_line
          margin-left: 1vw
          width: 50%
          border-radius: 1px
          border: 1px solid #FFFF
        h2
          margin-left: 1vw
          font-size: 0.9em
          font-weight: 400
          letter-spacing: 1.8px
          .bold_text
            font-weight: 700
  @media screen and ( max-width: 1024px )
    .wrapper
      background: url("../assets/third_block_mobile_bg.png") !important
      height: 140vh !important
      .header
        margin-left: 10vw !important
        margin-top: 9.5vh !important
        font-size: 3.2em !important
      .bot_handler
        margin-top: 8vh !important
        flex-direction: column !important
        justify-content: center !important
        align-items: center !important
        .text_block
          margin-bottom: 15% !important
          width: 80% !important
          height: 27vh !important
          padding: 2.5% !important
          h1
            margin-left: 2vw !important
            font-size: 1.55em !important
          .white_line
            margin-left: 2vw !important
            width: 50%
            border-radius: 1px
            border: 1px solid #FFFF
          h2
            margin-left: 2vw !important
            font-size: 1.08em
            font-weight: 400
            letter-spacing: 1.8px
            .bold_text
              font-weight: 700
</style>