<template>
<div class="item_wrapper">
    <div class="partner_item">
        <img v-bind:src="'../assets/'+ItemData.imgSource+'.png'">
        <h2>{{ItemData.text}}</h2>
  </div>
</div>
    
</template>

<script>
export default {
    props:["ItemData"]
    
}
</script>

<style lang="sass" scoped>

    .item_wrapper
        width: 25vw !important
        margin-left: 5vw
        display: flex
        float: left
        height: 22vh
        .partner_item
            width: 15vw
            height: 22vh
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
        .item_wrapper
            width: 100vw !important
            margin-left: 20vw !important
            .partner_item
                width: 60vw !important
</style>