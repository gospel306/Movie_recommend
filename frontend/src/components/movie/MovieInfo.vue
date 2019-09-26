<template>
  <v-container column justify-content="space-between">
    <v-layout>
      <v-flex xs8>
        <h1>나쁜 녀석들</h1>
        <v-flex>
          <v-layout>
            <h3>평점 :</h3>
            <v-rating
              :value="rating"
              color="indigo"
              background-color="indigo"
              half-increments
              dense
              readonly
            />
            <div class="grey--text ml-4">{{ rating.toFixed(1) }}</div>
          </v-layout>
        </v-flex>
        <v-flex>
          <v-layout>
            <h3>장르 :</h3>
            {{genre}}
          </v-layout>
        </v-flex>
      </v-flex>

      <v-flex xs4>
        <v-card
          :color="active ? undefined : 'grey lighten-1'"
          class="ma-4"
          height="400"
          width="300"
        ></v-card>
      </v-flex>
    </v-layout>

    <v-layout column>
      <h2>줄거리</h2>
      {{content}}
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      rating: 4,
      genre: "범죄 / 액션",
      content:
        "블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라블라"
    };
  },
  mounted(){
    alert(this.$route.params.id);
  }
};
</script>