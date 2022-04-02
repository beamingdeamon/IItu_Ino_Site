<template>
  <div class="wrapper">
    <img src="../assets/ino_logo.png" alt="">
    <div class="a_wrapper">
      <a href="#main">Главная</a>
      <a href="#about-us">О нас</a>
      <a href="#third">Что мы предлагаем?</a>
      <a href="#fourth">Что внутри?</a>
      <a href="#have-idea">Есть идея?</a>
      <a href="#partners">Наши партнеры</a>
    </div>
    
  </div>
</template>

<script>
export default {
    
}
</script>

<style lang="sass" scoped>
  .wrapper
    width: 100vw
    height: 80px
    display: flex
    align-items: center
    background-color: white
    z-index: 1000
    background: rgba(0, 0, 0, 0.2)
    backdrop-filter: blur(10px)
    font-family: 'Montserrat', sans-serif
    img
      margin-left: 11vw
    .a_wrapper
      font-size: 18px
      width: 60vw
      height: 100%
      margin-left: 20vw
      display: flex
      flex-direction: row
      align-items: center
      justify-content: space-around 
      a
        text-decoration: none
        color: white
        font-weight: 400
      a:active
        color: white
      a:hover
        text-decoration: underline
        font-weight: 600 !important
        text-decoration-thickness: 2px
  @media screen and ( max-width: 1024px )
    .wrapper
      display: none !important
    
</style>