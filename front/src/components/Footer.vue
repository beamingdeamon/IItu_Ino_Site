<template>
    <div class="footer_wrapper">
      <div class="items_wrapper">
        <div class="footer_item">
          <img src="../assets/adres.png" alt="">
          <div class="item_wrapper">
            <div class="footer_header">Адрес</div>
            <div class="footer_describe">г.Алматы<br>Манаса 34/1, МУИТ, 4 этаж</div>
          </div>
        </div>
        <div class="footer_item">
          <img src="../assets/contacts.png" alt="">
          <div class="item_wrapper">
            <div class="footer_header">Контакты</div>
            <div class="footer_describe">+7 (727) 244 51 03</div>
          </div>
        </div>
        <div class="footer_item">
          <img src="../assets/mail.png" alt="">
          <div class="item_wrapper">
            <div class="footer_header">Почта</div>
            <div class="footer_describe">itinocenter@gmail.com</div>
          </div>
        </div>
      </div>
      <div class="rights">
        © 2021 - 2022.<br> 
        All Right Reserved. IITU Innovation.
      </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="sass" scoped>
  .footer_wrapper
    width: 100vw
    height: 60vh
    background: url("../assets/footer_bg.png")
    background-size: cover
    background-position: center center
    display: flex
    flex-direction: column
    align-items: center
    justify-content: center
    font-family: 'Montserrat', sans-serif
    .rights
      color: white
      margin-top: 7vh
      margin-right: 70vw
    .items_wrapper
      margin-top: 10vh
      width: 90vw
      height: 35%
      display: flex
      flex-direction: row
      align-items: center
      justify-content: space-around
      .footer_item
        width: 27%
        height: 70%
        display: flex
        flex-direction: row
        color: white
        img
          width: 60px
          height: 60px
        .item_wrapper
          margin-left: 1vw
          margin-top: 1.5vh
          letter-spacing: 1px
          .footer_header
            font-size: 1.2em
          .footer_describe
            font-size: 1.25em
            font-weight: 700
            margin-top: 2.5vh
  @media screen and ( max-width: 1024px )
    .footer_wrapper
      height: 65vh !important
      background: url('../assets/footer_mobile_bg.png') !important
      .items_wrapper
        height: 60% !important
        flex-direction: column !important
        margin-top: 20vh !important
        .footer_item
          width: 100% !important
          img
            width: 45px
            height: 45px
          .item_wrapper
            margin-left: 4vw !important
            .footer_describe
              margin-top: 1vh !important
      .rights
        margin-right: 0 !important
        width: 90% !important
        margin-top: 0 !important

</style>
