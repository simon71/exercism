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
 # start by adding a class method
  class << self

    # def convert that needs to accept an argument
    def convert(raindrop_count)

      # start with an empty string
      output = ''

      # add Pling if raindrop_count is divisable by 3 (this says if raindrop_count / 3 leaves no remainder then output Pling)
      output << 'Pling' if raindrop_count % 3 == 0
      # add Plang if raindrop_count is divisable by 5
      output << 'Plang' if raindrop_count % 5 == 0
      # add Plong if raindrop_count is divisable by 7
      output << 'Plong' if raindrop_count % 7 == 0

      # if output is not empty return raindrop_count to string
      !output.empty? ? output : raindrop_count.to_s
    
    end
  end
end
