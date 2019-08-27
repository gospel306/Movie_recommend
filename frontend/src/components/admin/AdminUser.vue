<template>
  <v-container>
    <h1>영화 관리</h1>
    <v-layout justify-center text-xs-center row class="mb-5">
      <v-btn to="/adminuser" color="grey darken-2" class="white--text">유저관리</v-btn>
      <v-btn to="/adminmovie" color="grey darken-2" class="white--text">영화관리</v-btn>
      <v-spacer></v-spacer>
    </v-layout>

    <router-view></router-view>

    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="desserts"
      item-key="_id"
      select-all
      class="elevation-1 mb-3"
    >
      <template v-slot:items="props">
        <td>
          <v-checkbox v-model="props.selected" primary hide-details></v-checkbox>
        </td>
        <td>{{ props.item.nickname }}</td>
        <td class="text-xs-left">{{ props.item.id }}</td>
        <td class="text-xs-left">{{ props.item.name }}</td>
        <td class="text-xs-left">{{ props.item.department }}</td>
        <td class="text-xs-left">{{ props.item.position }}</td>
        <td class="text-xs-left">{{ props.item.membership }}</td>
      </template>
    </v-data-table>
    <v-card>
      <div class="getmembership">
        <v-select v-model="membership" label="등급" :items="memberships" required></v-select>
        <v-btn @click="updateUserMembership" color="grey darken-2" class="white--text">등급 변경</v-btn>
      </div>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      superdepartment: "",
      first: "",
      firsts: [],
      second: "",
      seconds: [],
      showbtn: true,
      pagination: {
        sortBy: "name"
      },

      membership: "회원",
      memberships: ["비회원", "회원", "관리자"],
      selected: [],
      headers: [
        {
          text: "닉네임",
          align: "left",
          value: "nickname"
        },
        { text: "아이디", value: "id" },
        { text: "이름", value: "name" },
        { text: "부서", value: "department" },
        { text: "기수", value: "position" },
        { text: "등급", value: "membership" }
      ],
      desserts: []
    };
  },
  mounted() {
  },
  methods: {
    
  }
};
</script>

<style>
</style>
