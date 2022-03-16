<template>
  <div class="wrapper">
    <div class="header">
    <div class="circle"></div>
      <h1>Есть идея?</h1>
      <h2>Поздравляем! У Вас есть идея, которая покорит мир или просто принесет вам прибыль. А мы поможем вам воплотить её в жизнь. <span class="bold">Возможно всё.</span></h2>
      <div class="cube"></div>
    </div>
    <div class="bottom_wrapper">
      <div class="left_block">
        <div class="number">1</div>
        <div class="opacity">
          <h1>Регистрация проектов презентаций (MVP)</h1>
          <h2>Симона окончила музыкальный колледж в Аржантее. Она записывала песни со второго курса колледжа. Творческий путь начался с местных концертов для друзей, а в прошлом году она дала три концерта в клубе Shiiiva.</h2>
        </div>
      </div>
      <div class="right_block">
        <div class="opacity">
          <h1>Отбор проектов</h1>
          <h2>Пол создал серию работ «За мостом», посетив крупнейшие европейские столицы. В экспозицию вошли фотографии из Берлина, Москвы, Барселоны, Варшавы и других городов.</h2> 
        </div>
        
          <div class="number">2</div> 
      </div>
      <div class="left_block">
        <div class="number">3</div>
        <div class="opacity">
          <h1>Питчинг лучших проектов</h1>
          <h2>Группа из Малаги, на юге Испании. Три сестры, которые играют <br>традиционную «cante jondo».</h2>

          </div>
      </div>
      <div class="right_block">
        <div class="opacity">
          <h1>Отбор проектов</h1>
          <h2>Пол создал серию работ «За мостом», посетив крупнейшие европейские столицы. В экспозицию вошли фотографии из Берлина, Москвы, Барселоны, Варшавы и других городов.</h2> 
        </div>
        
          <div class="number">4</div> 
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:"HaveIdea"
}
</script>

<style lang="sass" scoped>
  .wrapper
    width: 100vw
    height: 220vh
    background: url("../assets/idea_block_bg.png")
    background-size: cover
    background-position: center center
    color: white
    font-family: 'Montserrat', sans-serif
    .circle
      background: url("../assets/about_circle.png")
      background-size: cover
      background-position: center center
      position: absolute
      width: 40vw
      height: 80vh
      filter: blur(100px)
      margin-top: 85vh
      left: 48vw
      z-index: 0
    .header
      width: 100vw
      height: 20vh
      h1
        padding-top: 5.5vh
        margin-left: 7vw
        font-weight: 400
        font-size: 2.5em
        margin-top: 0
        width: 25vw
        letter-spacing: 4px
      h2
        margin-left: 7vw
        width: 43vw
        font-weight: 400
        font-size: 0.85em
        letter-spacing: 1px
        .bold
          font-weight: 600
      .cube
        background: url("../assets/about_cube.png")
        background-size: cover
        background-position: center center
        width: 6vw
        height: 10vh
        position: absolute
        left: 90vw
        margin-top: -13vh
        transform: rotate(-20deg)
    .bottom_wrapper
      width: 100vw
      height: 200vh
      display: flex
      align-items: center
      flex-direction: column
      .left_block
        height: 50vh
        width: 80%
        margin-left: 3vw
        display: flex
        flex-direction: row
        justify-content: space-between
        z-index: 100
        .number
          margin-top: 12vh
          font-style: italic
          margin-left: 2vw
          font-weight: 500
          font-size: 10em
          width: 10vw
          transform: rotate(-3.06deg)
          background: radial-gradient(#FFFFFF 0%, #6D8DFF 100%)
          -webkit-background-clip: text
          -webkit-text-fill-color: transparent
        .opacity
          margin-top: 9vh
          width: 79%
          height: 67%
          background: rgba(255, 255, 255, 0.1)
          backdrop-filter: blur(10px)
          border-radius: 20px
          h1
            margin-top: 6vh
            margin-left: 3vw
            font-weight: 600
            font-size: 2.3em
          h2
            margin-top: 4vh
            margin-left: 3vw
            line-height: 4.2vh
            font-weight: 400
            font-size: 1.1em
            width: 80%
      .right_block
        height: 50vh
        width: 76%
        display: flex
        flex-direction: row
        justify-content: space-between
        z-index: 100
        .number
          margin-top: 12vh
          font-style: italic
          float: right
          margin-right: 2.5vw
          font-weight: 500
          font-size: 10em
          width: 8vw
          transform: rotate(-3.06deg)
          background: radial-gradient(#FFFFFF 0%, #6D8DFF 100%)
          -webkit-background-clip: text
          -webkit-text-fill-color: transparent
          height: 30vh
        .opacity
          margin-top: 9vh
          width: 76%
          height: 67%
          background: rgba(255, 255, 255, 0.1)
          backdrop-filter: blur(10px)
          border-radius: 20px
          h1
            margin-top: 5vh
            margin-left: 3vw
            font-weight: 600
            font-size: 2.3em
          h2
            margin-top: 5vh
            margin-left: 3vw
            line-height: 4.2vh
            font-weight: 400
            font-size: 1.1em
            width: 80% 
  @media screen and ( max-width: 1024px )
    .wrapper
      background: url('../assets/have_idea_block_mobile_bg.png') !important
      height: 260vh !important
      .circle
        display: none !important
      .header
        width: 100vw
        height: 25vh
        h1
          padding-top: 8vh !important
          margin-left: 7vw
          font-weight: 400
          font-size: 3em !important
          margin-top: 0
          width: 100% !important
          letter-spacing: 4px
        h2
          width: 80% !important
          font-size: 1.1em !important
          line-height: 1.7 !important
        .cube
          display: none !important
      .bottom_wrapper
        height: 230vh !important
        .left_block
          height: 60vh !important
          width: 90% !important
          flex-direction: column !important
          .number
            margin-top: 10vh !important
            margin-left: 8% !important
            font-size: 16em !important
            width: 45% !important
            z-index: 0 !important
          .opacity
            margin-top: -8vh !important
            width: 100% !important
            height: 50vh !important
            z-index: 100 !important
            h1
              margin-top: 3vh !important
              font-size: 1.5em !important
              margin-left: 5vw !important
            h2
              margin-top: 2vh !important
              margin-left: 5vw !important
              line-height: 1.5 !important
              font-size: 1.1em !important
              width: 90% !important
        .right_block
          height: auto !important
          width: 90% !important
          flex-direction: column !important
          .number
            margin-top: 10vh !important
            margin-left: 8% !important
            font-size: 16em !important
            width: 45% !important
            order: 1 !important
            z-index: 0 !important
          .opacity
            order: 2 !important
            z-index: 100 !important
            margin-top: -8vh !important
            width: 100% !important
            height: 70% !important
            background: rgba(255, 255, 255, 0.1)
            backdrop-filter: blur(10px)
            border-radius: 20px
            h1
              margin-top: 3vh !important
              font-size: 1.5em !important
              margin-left: 5vw !important
            h2
              margin-top: 2vh !important
              margin-left: 5vw !important
              line-height: 1.5 !important
              font-size: 1.1em !important
              width: 90% !important
</style>
