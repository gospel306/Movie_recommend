<template>
  <v-container>
    <v-simple-table class="tab" >
      <thead>
        <tr>
          <th class="text-center">제목</th>
          <th class="text-center">평점</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="card in ratingListCardsSliced" :key="card.id">
          <td>{{ card.title }}</td>
          <td>
            <v-rating
              v-model="card.rating"
              color="black"
              background-color="black"
              readonly
              dense
            />
          </td>
        </tr>
      </tbody>
    </v-simple-table>
    <v-pagination color="black" class="page" v-if="maxPages > 1" v-model="page" :length="maxPages" />
  </v-container>
</template>

<script>

export default {
  components: {
    
  },
  props: {
    MyRatingItems: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
      cardsPerPage: 8,
      page: 1,
  }),
  computed: {
    ratingListEmpty: function() {
      return this.UserItems.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.MyRatingItems.length + this.cardsPerPage - 1) / this.cardsPerPage
      );
    },
    ratingListCardsSliced: function() {
      return this.MyRatingItems.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    },
  },
};
</script>
<style>
  .page{
    margin-top:20px;
  }
  .tab{
    width:450px;
  }
</style>