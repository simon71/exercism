##### Answer submitted to exercism #####
#
# class Acronyim
#   class << self
#     def abbreviate(words)
#       # .words to uppercase
#       # .split on any non-word characters
#       # .map the first letter of each split
#       # .join them together
#       words.upcase.split(/\W/).map{ |wrd| wrd[0]}.join
#     end
#   end
# end

##### Other Possible Answer #####
class Acronym
  def initialize(phrase)
    @phrase = String(phrase)
    @words = normalize(@phrase.split(/\W/))
  end

  def abbreviation
    @words.map{ |wrd| wrd[0]}.join
  end

  class << self
    def abbreviate(phrase)
      new(phrase).abbreviation
    end
  end

  private

  def normalize(phrase)
    phrase.upCase
  end
end
