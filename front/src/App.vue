<template>
  <div>
    <router-view/>
  </div>
</template>


<script>
export default {
  name:"App",
}
</script>

<style lang="sass">
body
  margin: 0
  padding: 0
  font-size: 2vh
  overflow-x: hidden
  *
    border: 1px solid red
  @media screen and ( max-width: 1024px )
    font-size: 1.6vh
</style>
