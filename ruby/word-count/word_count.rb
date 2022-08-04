class Phrase
  def initialize(phrase)
    # the regex in this scan looks for and words or ' inside of a word boundary \b
    @words = String(phrase).downcase.scan(/\b[\w']+\b/)
  end

  def word_count
  ##  Simple Option
  #   counts = {}

  #   @words.each do |word|
  #     counts[word] = 1 + counts[word].to_i
  #   end
  #   counts

    counts = @words.group_by(&:itself)
    counts.each { |k,v| counts[k] = v.count }

  end
end

# words = 'one fish two fish red fish blue fish'.split
# => ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
# words.group_by { |word| word}
# => {"one"=>["one"], "fish"=>["fish", "fish", "fish", "fish"], "two"=>["two"], "red"=>["red"], "blue"=>["blue"]}
# words.group_by { |word| word.itself }
#  => {"one"=>["one"], "fish"=>["fish", "fish", "fish", "fish"], "two"=>["two"], "red"=>["red"], "blue"=>["blue"]}
# words.group_by(&:itself)
#  => {"one"=>["one"], "fish"=>["fish", "fish", "fish", "fish"], "two"=>["two"], "red"=>["red"], "blue"=>["blue"]}
