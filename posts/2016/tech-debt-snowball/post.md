If you've never heard of a [Debt Snowball](https://www.daveramsey.com/blog/get-out-of-debt-with-the-debt-snowball-plan/) approach for getting out of debt created by [Dave Ramsey](https://en.wikipedia.org/wiki/Dave_Ramsey) you may find this title misleading. 

If you thought that this post will be about how tech debt can snow ball out of control, my appologies. I actually want to talk about a strategy that can be use to get out of tech debt.

{Picture of code red}

## What is a Debt Snowball?

[Dave Ramsey](https://en.wikipedia.org/wiki/Dave_Ramsey) teaches a simple but powerful idea to help people to get out of debt.

His advise - **pay off their smallest debts first**.

This advice may seem counterintuitive. Simple math would suggest paying off the **highest interest rate** debt first to minimize the financial loss.

Dave, however, argues that being in debt has much more to do with **human psychology**, than it has to do with math. 

**The main goal with using Dave's approach is to build up a good habit first.**

For example, let's assume a person has 3 debts: 
- $500 student loan - 5% Interest Rate - $50 Monthly payment
- $1000 car loan - 10% Interest Rate - $50 Monthly payment
- $1500 on credit card - 15% Interest Rate - $50 Monthly payment

Also, let's say this person has an extra $50 a month to help pay out the debt faster.

**Dave suggests paying off the student loan first!** 

With the original payment of $50 a month plus $50 extra, the person will be able to pay off $500 in studen debt in five months.


Five months later, with the student load gone, the person would now have the $100 that used to go towards the Student load freed up to be apply towards the car loan.

In addition, having one of their debts disappear the person is likely to feel great and motivated to keep going. 

The car loan by now shrank to $750 already from original $1000 - 5 months * regular $50 payment. With the new payment of $150 a month ($50 original payment + $100 newly freed up money from student load payment) the car load would only take 5 more month to pay off (5 months * $150 = $750).

Then the rest of the freed up funds can be used to tackle the last remaining debt.

This calculation leaves out the interested rates calculated during that time period, but the point is that the benefit of working with human nature and helping to build up a good habit and generate visible traction and momentum, greatly outweights whatever financial loss may be present from not paying off the highest interest first. 

## How does Debt Snowball translates to Tech Debt Snowball

Few weeks ago I began working on a medium size project that had close to zero unit test coverage. From that prespective the tech debt was pretty significant.

I've added the basic unit test and code coverage tools, but staring at the mountain of untested red code from my Istanbul report was very intimidating and I found myself feeling pretty depressed about the whole ordeal.

Earlier that week, I've fixed a small bug in the project and added one unit test to make sure my functionality was working.

Since, I already had a bit of work done in one file, I've decided to apply Dave's principle of Debt Snowball to my test coverage and aimed for a 100% code coverage in that one file.

The file that I decided to start with, was not the most important file in the project. There was not a really good reason to start there, except for the fact that I'v already had a little bit of traction there.

Within a day I had 100% unit test code coverage in the file and I've felt much better about the project. In addition, it gently forced me to explore other parts of the project, which allowed me to feel less intimidated by the entire code base. 

{picture code gree}

Having had this one file to go from red to green (in terms of code coverage) really helped me to have a positive outlook on the entire exercise. I went from being depressed about having to write unit tests, to feeling like it was a game of sorts and **I was winning**.

I was excited and motivated to get my code coverage up and I felt good about it in the process. 

I am confident and optimistic that in the due time we'll be able to get coverage for the entire project to a healthy percentage.

## Conclusion

I blieve that the principles of Debt Snowball can be applied well to reducing the Tech Debt. 

It helps to pay off the smallest tech debt first, allowing the team to make vissible progreass. Overtime the team will be able tackle bigger tech debt, while continuing to develope the culture of writing maintainable code.