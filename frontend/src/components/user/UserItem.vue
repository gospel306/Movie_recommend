<template>
  <v-container>
    <v-simple-table>
      <thead>
        <tr>
          <th class="text-center">name</th>
          <th class="text-center">gender</th>
          <th class="text-center">age</th>
          <th class="text-center">detail</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="card in userListCardsSliced" :key="card.id">
          <td>{{ card.username }}</td>
          <td>{{ card.gender }}</td>
          <td>{{ card.age }}</td>
          <td>
            <UserDetail
              :id="card.id"
              :age="card.age"
              :gender="card.gender"
              :is_staff="card.is_staff"
              :occupation="card.occupation"
              :username="card.username"
            />
          </td>
        </tr>
      </tbody>
    </v-simple-table>
    <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
  </v-container>
</template>

<script>
import UserDetail from "@/components/user/UserDetail";

export default {
  components: {
    UserDetail
  },
  props: {
    UserItems: {
      type: Array,
      default: () => new Array(),
    },
  },
  data: () => ({
      cardsPerPage: 10,
      page: 1,
  }),
  computed: {
    userListEmpty: function() {
      return this.UserItems.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.UserItems.length + this.cardsPerPage - 1) / this.cardsPerPage
      );
    },
    userListCardsSliced: function() {
      return this.UserItems.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    },
  },
};
</script>