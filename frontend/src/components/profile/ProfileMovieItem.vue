<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    {{ title }}
                  </v-list-item-title>
                  <v-list-item-subtitle>{{ genreSplit }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-card-text>
                <v-layout justify-center>
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
              </v-card-text>
              <v-card-text>
                <v-layout justify-center>
                  <v-icon color="black">mdi-eye</v-icon>
                  <div class="grey--text ml-4">{{ viewCnt }}</div>
                </v-layout>
              </v-card-text>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
      <v-btn color="primary" class="ma-2" dark @click="dialog = true">평점 작성</v-btn>
      <v-dialog v-model="dialog" persistent max-width="300">
        <v-card>
          <v-layout justify-center>
            <v-card-title class="headline">이 영화의 점수는?</v-card-title>
          </v-layout>
            <v-card-text>
                <v-layout justify-center>별점을 매겨주세요!</v-layout>
            </v-card-text>
          <v-layout justify-center>
          <v-rating
            :value="rating2"
            color="indigo"
            background-color="indigo"
            half-increments            
          />
          </v-layout>
          <v-card-actions>
            <div class="flex-grow-1"></div>
            <v-btn color="green darken-1" text @click="submit()">완료</v-btn>
            <v-btn color="green darken-1" text @click="dialog = false">취소</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </v-hover>
</template>

<script>

export default {
  data(){
      return {
            ratings:{
                userid:this.$session.get('id'),
                movieid:this.id,
                rating:this.rating2,
                timestamp:123456789
            },
            dialog:false
      }
  },
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: String,
      default: ""
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    rating2: {
      type: Number,
      default: 0.0
    },                                                                                                                                                                        
    viewCnt: {
      type: Number,
      default: 0
    },
    check:{
      type: Boolean,
      default : true,
    }
  },
  computed: {
    genreSplit() {
      var str = this.genres
      return str.replace(/\|/g," / ")
    }
  },
  components: {
    
  },
  methods:{
    submit: function(rating){
        alert(this.ratings.userid);
        alert(this.ratings.movieid);
        alert(this.ratings.rating);
        axios.post(
            this.$stroe.server + "/api/ratings/"
            +"&movieid="+this.id
            +"&rating="+rating
        )
        this.dialog = false;
    },

    modifyInfo: function(id){
        axios.put(
            this.$store.state.server + "/api/users/?id=" + id
            +"&gender="+this.items.gender
            +"&age="+this.items.age
            +"&occupation="+this.items.occupation
        )
        .then(() => {
            this.updateDialog = false;
            router.push("/profileInfo");
        });
    }
  }
};
</script>