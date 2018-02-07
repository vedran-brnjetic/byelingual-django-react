import React, {Component} from 'react';
import {
    Carousel,
    CarouselItem,
    CarouselControl,
    CarouselIndicators,
    CarouselCaption
} from 'reactstrap';

const items = [
{
    src: 'http://www.timelinecoverbanner.com/facebook-covers/2012/01/old-paper-vintage.jpg',
    altText: 'Byelingual Game Platform',
    caption: 'Byelingual Game Platform'
  },
  {
    src: 'http://www.timelinecoverbanner.com/facebook-covers/2012/01/old-paper-vintage.jpg',
    altText: 'Cabin in The Woods',
    caption: 'Cabin in The Woods'
  },
  {
    src: 'http://www.timelinecoverbanner.com/facebook-covers/2012/01/old-paper-vintage.jpg',
    altText: 'Slide 3',
    caption: 'Story 3'
  }
];

class ByeCarousel extends Component {
  constructor(props) {
    super(props);
    this.state = { activeIndex: 0 };
    this.next = this.next.bind(this);
    this.previous = this.previous.bind(this);
    this.goToIndex = this.goToIndex.bind(this);
    this.onExiting = this.onExiting.bind(this);
    this.onExited = this.onExited.bind(this);
  }

  onExiting() {
    this.animating = true;
  }

  onExited() {
    this.animating = false;
  }

  next() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === items.length - 1 ? 0 : this.state.activeIndex + 1;
    this.setState({ activeIndex: nextIndex });
  }

  previous() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === 0 ? items.length - 1 : this.state.activeIndex - 1;
    this.setState({ activeIndex: nextIndex });
  }

  goToIndex(newIndex) {
    if (this.animating) return;
    this.setState({ activeIndex: newIndex });
  }


  render() {
    const { activeIndex } = this.state;
    const imgStyle = {
        width:'100%',
        height:'60%',

    }
    const slides = items.map((item) => {
      return (
        <CarouselItem
          onExiting={this.onExiting}
          onExited={this.onExited}
          key={item.caption}
        >
          <img style={imgStyle} src={item.src} alt={item.altText} />
          <CarouselCaption captionText={item.caption} captionHeader={item.caption} />
        </CarouselItem>
      );
    });

    return (
      <div>
      <Carousel id="carousel"
        activeIndex={activeIndex}
        next={this.next}
        previous={this.previous}
      >
        <CarouselIndicators items={items} activeIndex={activeIndex} onClickHandler={this.goToIndex} />
        {slides}
        <CarouselControl direction="prev" directionText="Previous" onClickHandler={this.previous} />
        <CarouselControl direction="next" directionText="Next" onClickHandler={this.next} />
      </Carousel>
      <hr />

      </div>
    );
  }
}

export default ByeCarousel;
