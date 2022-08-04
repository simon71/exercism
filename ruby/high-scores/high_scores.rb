class HighScores

  attr_reader :scores

  def initialize(scores)
    @scores=Array(scores)
  end

  def latest
    @scores.last
  end

  def personal_best
    @scores.max
  end

  def personal_top_three
    @scores.sort.reverse.first(3)
  end

  def latest_is_personal_best?
    if @scores.last != @scores.max
      false
    else
      true
    end
  end

end
