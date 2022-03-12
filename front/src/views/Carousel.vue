<template>
    <div class="wrapper">
        <div class="header">Наши партнеры</div>
        <div class="carousel"
        :style="{'margin-left':'-' + (100 * visibleSlide)+ '%'}">
        <CarouselItem 
        v-for="item in ItemData"
        :key="item.id"
        :ItemData="item"
        />
        </div>
    </div>
</template>

<script>
import CarouselItem from '../components/CarouselItem.vue'
export default {
    props: {
        ItemData:{
            type: Array,
            default:() => []
        },
        interval:{
            type: Number,
            default: 0
        }
    },
        data(){
        return{
            visibleSlide: 0
        }
    },
    components:{
        CarouselItem
    },
    methods:{
        nextSlide(){
            if(this.ItemData.length % 4 === 0){
                if(this.visibleSlide === parseInt(this.ItemData.length / 4) - 1){
                    this.visibleSlide = 0
                }else{
                    this.visibleSlide++;
                }
            }else{
            if(this.visibleSlide === parseInt(this.ItemData.length / 4)){
                    this.visibleSlide = 0
                }else{
                    this.visibleSlide++;
                }
            }
                
        }
    },
    mounted() {
    if(this.interval > 0){
            let vm = this
            setInterval(function() {
                vm.nextSlide()
            }, vm.interval)
        }
    },
}
</script>

<style lang="sass" scoped>
    .wrapper
        border: 1px solid red
        background: url("../assets/partners_block_bg.png")
        background-size: cover
        background-position: center center
        height: 80vh
        font-family: 'Montserrat', sans-serif
        display: flex
        flex-direction: column
        align-items: center
        width: 100vw
        overflow: hidden
        z-index: 0
        .header
            margin-top: 12vh
            width: 76vw
            color: black
            font-weight: 400
            font-size: 4em
        .carousel
            width: 80vw
            height: 50vh
            display: flex
            flex-direction: row
            align-items: center
            transition: all ease 1s
  @media screen and ( max-width: 1024px )
    .wrapper
      background: url('../assets/partner_block_mobile_bg.png') !important
      height: 60vh !important
      .header
        margin-top: 8vh !important
        width: 90% !important
        font-size: 3.5em !important
</style>