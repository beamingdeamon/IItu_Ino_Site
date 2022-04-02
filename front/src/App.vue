<template>
  <div>
    <Header  class="header"/>
    <router-view/>
    <Footer />
  </div>
</template>


<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
export default {
  name:"App",
  components:{
    Header,
    Footer
  }
}
</script>

<style lang="sass">
body
  margin: 0
  padding: 0
  font-size: 2vh
  overflow-x: hidden
  // *
  //   border: 1px solid red
  .header
    position: fixed
  @media screen and ( max-width: 1024px )
    font-size: 1.6vh
</style>
