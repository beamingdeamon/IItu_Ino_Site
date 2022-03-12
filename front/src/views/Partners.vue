<template>
  <div class="wrapper">
    <div class="header">Наши партнеры</div>
    <div class="items_wrapper">
      <PartnerItem class="partner_item"
      v-for="item in partner" 
			:key="item.id" 
			:ItemData = "item"/>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueCarousel from 'vue-carousel'
import PartnerItem from '../components/PartnerItem.vue'
export default {
  name: "Partners",
  data() {
    return {
      partner: []
    };
	},components:{
    'carousel': VueCarousel.Carousel,
    'slide': VueCarousel.Slide,
    PartnerItem
  },
  mounted(){
    axios.get('http://localhost:8000/api/getpartners/')
      .then(response => (this.partner = response.data));
  },
}
</script>
  
<style lang="sass" scoped>
  .wrapper
    background: url("../assets/partners_block_bg.png")
    background-size: cover
    background-position: center center
    width: 100vw
    height: 80vh
    font-family: 'Montserrat', sans-serif
    display: flex
    flex-direction: column
    align-items: center
    .header
      margin-top: 12vh
      width: 76vw
      color: black
      font-weight: 400
      font-size: 4em
    .items_wrapper
      width: 80vw
      height: 50vh
      display: flex
      flex-direction: row
      justify-content: space-around
      align-items: center
      .partner_item
        width: 20%
        height: 50%
        background: rgba(18, 17, 26, 0.6)
        backdrop-filter: blur(8px)
        border-radius: 10px
        img
          margin-top: 12%
          margin-left: 10%
        h2
          margin-left: 10%
          margin-top: 10%
          color: white
          font-weight: 400
  @media screen and ( max-width: 1024px )
    .wrapper
      background: url('../assets/partner_block_mobile_bg.png') !important
      height: 60vh !important
      .header
        margin-top: 8vh !important
        width: 90% !important
        font-size: 3.5em !important
</style>
