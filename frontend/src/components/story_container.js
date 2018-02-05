import React, {Component} from 'react';
import {
	Card,
	Button,
	CardImg,
	CardTitle,
	CardText,
	CardDeck,
	CardBody
} from 'reactstrap';

class StoryContainer extends Component
{
	constructor(props){
		super(props);
    	this.state = {
      	error: null,
      	isLoaded: false,
      	stories: []
    	};
	}

	componentWillMount() {
		fetch("http://api.byelingual.me:8000/stories/")
			.then( res => res.json())
			.then(
				(result) => {
					this.setState({
						isLoaded: true,
						stories: result.stories
					});
				},
				(error) => {
					this.setState({
						isLoaded: true,
						error
					});
				}
			)
	}

   render () {
   	let {error, isLoadad, stories } = this.state;
   	if (error) {
			return <div>Error: { error.message }</div>;
   	}
   	else if(!isLoadad){
			return (
		    	<CardDeck className="col-md-12">
		    		{
		    			stories.map(
		    				story => (
      						<Card key={story.name}>
        						<CardImg top width="100%" src={ "http://byelingual.me:8000/media/" + story.image } alt={ story.description } />
        						<CardBody>
          						<CardTitle>{ story.name }</CardTitle>
          						<CardText>{ story.description }</CardText>
          						<Button disabled>Buy Now!</Button>
       							</CardBody>
      						</Card>
      					)
      				)
   				}
    			</CardDeck>
			);
   	}




	};
}
export default StoryContainer;
