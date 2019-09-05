<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="card in movieListCardsSliced" :key="card.id" pa-2>
        <MovieItem
          :id="card.id"
          :img="card.img"
          :title="card.title"
          :genres="card.genres"
          :rating="card.average_rating"
          :view-cnt="card.view_cnt"
          :check="check"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import MovieItem from "@/components/movie/MovieItem"
export default {
  components: {
    MovieItem
  },
  props: {
    MovieItems: {
      type: Array,
      default: () => new Array(),
    },
    check:{
      type: Boolean,
      default : true,
    }
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1,
  }),
  computed: {
    // pagination related variables
    movieListEmpty: function() {
      return this.MovieItems.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.MovieItems.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    movieListCardsSliced: function() {
      return this.MovieItems.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  },
};
</script>