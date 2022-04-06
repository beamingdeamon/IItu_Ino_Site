<template>
    <Carousel
        :ItemData = "partners"
        :interval = "2500"/>
</template>

<script>
import axios from 'axios'
import Carousel from './Carousel.vue'
export default {
    data(){
        return{
            partners: new Array()
        }
    },
    components: {
        Carousel
    },
    mounted(){
        axios.get('https://ino.iitu.kz/api/getpartners/')
        .then( response => {this.partners = response.data} )
        .catch(function (error) {
        console.log(error);
        })
    }
}
</script>

<style lang="sass" scoped>

</style>