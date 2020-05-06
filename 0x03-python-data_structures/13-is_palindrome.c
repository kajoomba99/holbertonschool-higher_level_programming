#include "lists.h"
/**
 * is_palindrome - is_palindrome
 * @head: head
 * Return: return
 */
int is_palindrome(listint_t **head)
{
	listint_t *comi = *head;
	listint_t *comf = *head;
	listint_t *tl = *head;
	int counter = 0;
	int dec = 1;
	int x = 0;

	while (tl != NULL)
	{
		counter += 1;
		tl = tl->next;
	}

	while (comi != NULL)
	{
		x = 0;
		comf = *head;
		while (x < (counter - dec))
		{
			comf = comf->next;
			x += 1;
		}
		dec += 1;
		if (comi->n != comf->n)
			return (0);
		comi = comi->next;
	}
	return (1);
}
