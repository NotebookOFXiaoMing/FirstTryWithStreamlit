header = st.container()
dataset = st.container()
feature = st.container()
model_training = st.container()


with header:
    st.title("Hello, My name is MingYan")
    st.text("In this project I took into the transactions of taxis in NYC. ...")


with dataset:
    st.header("NYC taxi dataset")
    st.text("I found this dataset on blablabla.com")

    dat01 = pd.read_csv("../data/iris.csv")
    st.write(dat01.head())

    st.subheader("Pick-up")

with feature:
    st.header("The features I created")

with model_training:
    st.header("Time to train the model!")
    st.text("Here You Got to chose some")
