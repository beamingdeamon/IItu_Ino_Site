<template>
  <div class="wrapper">
    <div class="header">Наши партнеры</div>
    <div class="items_wrapper">
      <PartnerItem 
      v-for="item in partner" 
			:key="item.id" 
			:ItemData = "item"/>
      
      <div class="partner_item">
        <img src="../assets/smart_point.png">
        <h2>SmArt.Point</h2>
      </div>
      <div class="partner_item">
        <img src="../assets/chevron.png">
        <h2>Chevron</h2>
      </div>
      <div class="partner_item">
        <img src="../assets/kolesa.png">
        <h2>Kolesa Group</h2>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PartnerItem from './PartnerItem.vue'
export default {
  name: "Partners",
  data() {
    return {
      partner: []
    };
	},components:{
    PartnerItem
  },
  mounted(){
    axios
      .get('http://localhost:8000/api/getpartners/')
      .then(response => (this.partner = response.data));
  }
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
</style>
