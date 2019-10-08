<template>
    <v-container>
      <v-layout column align-center>        
        <v-flex sm4>
          <v-img class="ck"
            src="../images/intro.gif" 
            width="400"
            height="166"
          ></v-img>
        </v-flex>
        <v-flex class="under">
          <v-layout text-sm-right >
            <v-flex class="pa-1">
              <v-icon large color="black">mdi-magnify</v-icon>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex class="str">
          <h1>이 곳은 빅데이터 기반의 '영화 추천 사이트'입니다.</h1>
        </v-flex>
      </v-layout>
    </v-container>
</template>


<script>
export default {
  name: "intropage",
  data: () => ({

  }),
  methods: {
  },
};
</script>

<style>
.ck{
  border-width: 1px;
  border-style: solid;
  border-color: white;
  border-radius: 15px;
  filter: grayscale(100%);
}
.under{
  border-width: 10px 10px 10px 10px;
  border-style: solid;
  border-color: black;
  margin-top: 60px;
  border-radius: 15px 15px 0px 15px; 

  width: 400px;
  height: 60px;  
}
.str{
  border-width: 0px 0px 3px 0px;
  border-style: solid;
  border-color: black;
  margin-top: 60px;
}
</style>

