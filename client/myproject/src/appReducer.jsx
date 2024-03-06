
export default function appReducer(store = {}, action) {
    switch (action.type) {

        case 'LOAD':
            console.log(action.payload)
            return action.payload;

        //movies:

        case 'ADD_MOVIE':
            const newMovie = action.payload
            const moviesCopy = store.movies
            return { ...store, movies: [...moviesCopy, newMovie] }; // Add new movie to movies list

        case 'UPDATE_MOVIE':
            const relevantIdToUpdate = action.payload._id
            const moviesCopyToUpdate = store.movies
            const finalMoviesAfterUpdate = moviesCopyToUpdate.map((movie) => movie._id === relevantIdToUpdate ? action.payload : movie);
            return { ...store, movies: finalMoviesAfterUpdate }


        case 'DELETE_MOVIE':
            const relevantIdToDlt = action.payload
            const moviesCopyToDlt = store.movies
            const finalMoviesAfterDlt = moviesCopyToDlt.filter((m) => m._id !== relevantIdToDlt)
            return { ...store, movies: finalMoviesAfterDlt }

        //subscriptions:

        case 'ADD_SUB':
            const newSubscription = action.payload
            const subscriptionsCopy = store.subscriptions
            return { ...store, subscriptions: [...subscriptionsCopy, newSubscription] };



        default:
            return store;

    }
}
