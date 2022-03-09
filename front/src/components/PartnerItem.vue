<template>
  <div class="partner_item">
    {{ItemData.imgSource}}
    <img v-bind:src="'../assets/'+ItemData.imgSource+'.png'">
    <h2>{{ItemData.text}}</h2>
  </div>
</template>

<script>
export default {
  name: "PartnerItem",
   data: () => ({
    }),
  proprs:{
    ItemData:{
      type: Object,
      default: () => {}
    }
  },
}
</script>

<style lang="sass" scoped>
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
