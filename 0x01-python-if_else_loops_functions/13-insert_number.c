#include "lists.h"
/**
 * insert_node - insert_node
 * @head: head
 * @number: number
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (temp != NULL)
	{
		if (temp->next->n > number)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			break;
		}
		if (temp->next == NULL)
		{
			temp->next = new_node;
			break;
		}
		temp = temp->next;
	}

	return (new_node);
}
