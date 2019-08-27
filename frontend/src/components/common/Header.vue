<template>
  <v-app-bar app clipped-left color="indigo">
    <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
    <span class="title ml-3 mr-5 white--text">영화 추천 서비스</span>
    <v-spacer />
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      drawer: null
    };
  }
};
</script>
