=begin
Convert a number to a string, the contents of which depend on the number's factors.

    If the number has 3 as a factor, output 'Pling'.
    If the number has 5 as a factor, output 'Plang'.
    If the number has 7 as a factor, output 'Plong'.
    If the number does not have 3, 5, or 7 as a factor, just pass the number's digits straight through.

Examples

    28's factors are 1, 2, 4, 7, 14, 28.
        In raindrop-speak, this would be a simple "Plong".
    30's factors are 1, 2, 3, 5, 6, 10, 15, 30.
        In raindrop-speak, this would be a "PlingPlang".
    34 has four factors: 1, 2, 17, and 34.
        In raindrop-speak, this would be "34"
=end
class Raindrops

  # first create a constant hash
  CONVERSIONS = {
    3 => 'Pling',
    5 => 'Plang',
    7 => 'Plong'
  }

  # attr_reader allows you to see the varibles defined in the  class, without this you would have to define them as a variable
  attr_reader :raindrop_count

  def initialize(raindrop_count)
    @raindrop_count = raindrop_count
  end

 # start by adding a class method
  class << self

    # def convert that needs to accept an argument
    def convert(raindrop_count)
      new(raindrop_count).convert
    end
  end

  def convert
    # this says of output doesn't return empty the convert to a string
      !output.empty? ? output : raindrop_count.to_s

## Non filtered way ##
=begin
    # start with an empty string
    output = ''
    # add Pling if raindrop_count is divisable by 3 (this says if raindrop_count / 3 leaves no remainder then output Pling)
    output << CONVERSIONS[3] if factor? 3
    # add Plang if raindrop_count is divisable by 5
    output << CONVERSIONS[5] if factor? 5
    # add Plong if raindrop_count is divisable by 7
    output << CONVERSIONS[7] if factor? 7

    # if output is not empty return raindrop_count to string
    !output.empty? ? output : raindrop_count.to_s
=end

  end

  # Define the factor calculation
  def factor?(number)
    raindrop_count % number == 0
  end
  def output
    ## Using Filters ##
      output = CONVERSIONS
        .filter { |factor, _| factor? factor}
        .values
        .join
  end

end
