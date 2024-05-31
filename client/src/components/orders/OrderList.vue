<template>
  <Header />
  <div class="container mt-4">
    <div class="row">
      <div class="col-md-10">
        <h2 class="mb-4">Orders</h2>
      </div>
      <div class="col-md-2">
        <button class="btn btn-md btn-outline-dark m-auto float-end" @click="addOrder">
          <strong>Add Order</strong>
        </button>
      </div>
    </div>
    <div v-if="orders.length == 0" class="text-center">
      <h5>No orders available.</h5>
    </div>
    <div v-for="order in orders" :key="order.id">
      <OrderView 
        :order="order" 
        @editOrder="editOrder" 
        @completeOrder="completeOrder" 
      />
    </div>
  </div>
  <Footer />
  <EditCard
    :order="orderData" 
    :isVisible="isModalVisible"
    :isNew="isNewOrder"
    @closeCard="closeModal"
    @updateOrder="updateOrder" />
</template>

<script>
import OrderView from './OrderView.vue'
import EditCard from './EditCard.vue'

export default {
  components: {
    OrderView,
    EditCard
  },
  data() {
    return {
      orders: [],
      orderData: {},
      isModalVisible: false,
      isNewOrder: false,
    };
  },
  methods: {
    fetchOrders() {
      this.$axios.post('/api/orders/get_list')
        .then(response => {
          this.orders = response.data;
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    },
    openModal(orderId) {
      if (orderId) {
        this.$axios.post('/api/orders/get/' + orderId)
          .then(response => {
            this.orderData = response.data;
          })
          .catch(error => {
            this.$toast.error('Something was wrong...');
          });
      }
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
      this.orderData = {};
    },
    addOrder() {
      this.isNewOrder = true;
      this.openModal();
    },
    editOrder(orderId) {
      this.isNewOrder = false;
      this.openModal(orderId);
    },
    updateOrder(updatedOrder) {
      this.$axios.post('/api/orders/save', updatedOrder)
        .then(response => {
          if (response.data.result) {
            this.$toast.success('Success!');
            this.closeModal();
            this.fetchOrders();
          } else {
            this.$toast.error(response.data.error);
          }
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    },
    completeOrder(orderId) {
      this.$axios.post('/api/orders/complete/' + orderId)
        .then(response => {
          if (response.data.result) {
            this.$toast.success('Success!');
            this.fetchOrders();
          } else {
            this.$toast.error(response.data.error);
          }
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    }
  },
  mounted() {
    this.fetchOrders();
  }
};
</script>